const express = require('express');
const app = express();
const fs = require('fs');
const path = require('path');
const PORT = process.env.PORT || 80;

const { db, initdb } = require('./db');
const authMiddleware = require('./handler');


// Parse JSON bodies
app.use(express.json());
app.use(express.urlencoded({ extended: true }));


// Set up EJS as the view engine
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));


// GET index page
app.get('/', authMiddleware, async (req, res) => {
	const userId = req.userId;

	if (userId){
		// logged in
		const query = await db.raw(
			`SELECT * FROM secrets WHERE owner_id = ?`,
			[userId]
		);

		return res.render('my_secrets', {secrets: query.rows});
	}
	else {
		// if not yet login
		return res.render('index', {message: null, error: null});
	}
});

// GET login page
app.get('/login', (req, res) => {
	return res.render('login', {message: null, error: null});
});

// GET signup page
app.get('/signup', (req, res) => {
	return res.render('signup', {message: null, error: null});
});

// GET create new secret page
app.get('/secrets/create', authMiddleware, (req, res) => {
	return res.render('create_secret');
});

// POST login
app.post('/login', async (req, res) => {
	const { username, password} = req.body;

	const userResult = await db.raw(
		`SELECT * FROM users WHERE username = ? AND password = ? LIMIT 1`, 
		[username, password]
	);

	// check user
	const user = userResult.rows[0];
	if(!user){
		return res.render('login', {message: null, error: 'User Not Found or The password is wrong'});
	}


	// check token
	const tokenQuery = await db.raw(
		`SELECT id FROM tokens WHERE user_id = ? AND expired_at > NOW()`,
		[user.id]
	);

	let token = tokenQuery.rows[0]?.id;
	if(!token){
		// no valid token: create one
		const createTokenQuery = await db.raw(
			`INSERT INTO tokens(user_id) VALUES (?) RETURNING id`,
			[user.id]
		);

		token = createTokenQuery.rows[0].id;
	}

	res.cookie('auth_token', token);
	return res.redirect('/');
});

// POST signup
app.post('/signup', async (req, res) => {
	const { username, password} = req.body;


	const userResult = await db.raw(
		`SELECT * FROM users WHERE username = ? LIMIT 1`, 
		[username]
	);

	if (userResult.rows.length >= 1){
		// user exist
		return res.render('signup', {message: null, error: 'Username already exists'});
	}

	const createUserQuery = await db.raw(
		`INSERT INTO users(username, password) VALUES (?, ?)`, 
		[username, password]
	);

	// render to login page: create user only, not logging in automatically
	return res.render('login', {message: 'Create User Successful', error: null});
});


app.post('/logout', async (req, res) => {
	res.clearCookie('auth_token');
	return res.redirect('/');
});

app.post('/secrets/create', authMiddleware, async (req, res) => {
	const userId = req.userId;
	if (!userId){
		// if user didn't login, redirect to index page
		res.clearCookie('auth_token');
		return res.redirect('/');
	}

	const content = req.body.content;
	const query = await db.raw(
		`INSERT INTO secrets(owner_id, content) VALUES ('${userId}', '${content}')` 
	);

	return res.redirect('/');
});

(async () => {
	// Ensure DB is ready before server runs
	await initdb();

	app.listen(PORT, ()=> {
		console.log(`Server running on port ${PORT}`)
	});
})();
