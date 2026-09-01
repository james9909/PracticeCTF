const { db } = require('./db');

// token hanlder
const getCookies = (cookieHeader) => {
	if (!cookieHeader) return {};
	return Object.fromEntries(
		cookieHeader.split(';').map(cookie => {
			const [key, ...value] = cookie.trim().split('=');
			return [key, decodeURIComponent(value.join('='))];
		})
	);
};

const authMiddleware = async (req, res, next) => {
	const cookies = getCookies(req.headers.cookie);
	const token = cookies.auth_token;

	if (!token) { return next(); }

	try {
		const query = await db.raw(
 			`SELECT * FROM tokens WHERE id = ? AND expired_at > NOW()`,
 			[token]
 		);

		if(query.rows.length <= 0) {
			res.clearCookie('auth_token');
			return res.render('index', {message: null, error: 'Invalid or expired token'});
		}

		// valid token
		req.userId = query.rows[0].user_id;
		return next()
	} catch (err){
		res.clearCookie('auth_token');
		console.log(`Server Internal Error: ${err}`)
		return res.render('index', {message: null, error: `Server Internal Error`});
	}
};

module.exports = authMiddleware;
