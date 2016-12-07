
const firebase = require('firebase');
const needle = require('needle');
const _ = require('lodash');

const config = require('./config/config');

const app = firebase.initializeApp(config);
const database = app.database();

module.exports = {
    /**
     * Ensure that a URL is provided.
     */
    parseURL(url, cb) {
        if (! url) {
            throw 'No URL provided.';
        }

        needle.get(url, (err, res, data) => {
            if (err || res.statusCode !== 200) {
                throw 'Error! Status code: ' + res.statusCode + ' (' + err.message + ')';
            }

            _.forEach(data, (words, category) => {
                if (! Array.isArray(words)) {
                    throw 'something is not in array format.';
                }
            });

            cb(data);
        });
    },
    
    /**
     * Persist the words to the database
     */
    persistWords(words) {
        _.forEach(words, (words, category) => {
            database.ref(category).set(_.uniq(words));
        });
    }
}
