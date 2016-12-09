/* eslint-disable no-console */

const express = require('express');
const app = express();
const PORT = 3002;
const path = require('path');

app.get('/', (req, res) => {
  res.send('Home');
});

app.use('/cities', express.static(path.join(__dirname, 'cities.json')));

app.listen(PORT, () => {
  console.log('Server listening at port ', PORT);
});
