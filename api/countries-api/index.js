/* eslint-disable no-console */

const express = require('express');
const app = express();
const PORT = 3005;
const path = require('path');

app.get('/', (req, res) => {
  res.send('Home');
});

app.use('/countries', express.static(path.join(__dirname, 'countries.json')));

app.listen(PORT, () => {
  console.log('Server listening at port ', PORT);
});
