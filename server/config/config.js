require('dotenv').config({ silent: true });

module.exports = {
    apiKey: process.env.API_KEY,
    authDomain: process.env.PROJECT_ID,
    databaseURL: process.env.DATABASE_URL
}