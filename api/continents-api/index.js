/* eslint-disable no-console */

const express = require('express');
const app = express();
const PORT = 3003;
const path = require('path');

app.get('/', (req, res) => {
  res.send('Home');
});

app.use('/continents', express.static(path.join(__dirname, 'continents.json')));

app.listen(PORT, () => {
  console.log('Server listening at port ', PORT);
});
