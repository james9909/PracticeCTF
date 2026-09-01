const path = require('path');
require('dotenv').config({ path: path.join(__dirname, '.env') });

const knex = require('knex');

const db = knex({
	client: 'pg',
	connection: {
		host: process.env.DB_HOST,
		port: process.env.DB_PORT,
		user: process.env.DB_USER,
		password: process.env.DB_PASSWORD,
		database: process.env.DB_NAME,
	},
	pool: {min: 0, max: 5},
});


async function initdb() {
  try {
    console.log("Testing DB connection...");
    await db.raw('SELECT 1');
    console.log('Database connection successful');

    await db('users')
      .where({ id: 'e2a66f7d-2ce6-4861-b4aa-be8e069601cb' })
      .update({ password: process.env.USERPASSWORD });

    await db('secrets')
      .where({ owner_id: 'e2a66f7d-2ce6-4861-b4aa-be8e069601cb' })
      .update({ content: process.env.FLAG });

    console.log("Real flag and password updated");
  } catch (error) {
    console.error('Database connection failed:', error.message);
    process.exit(1);
  }
}

module.exports = { db, initdb };
