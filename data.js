const firebase = require('./server/firebase');

const url = process.argv[2] || null;

try {
    firebase.parseURL(url, (words) => {
        firebase.persistWords(words);
        console.log('All done!');
    });
} catch (e) {
    console.log(e);
}
