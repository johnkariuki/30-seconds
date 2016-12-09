/* eslint-disable no-console */

const express = require('express');
const app = express();
const PORT = 3004;
const path = require('path');

app.get('/', (req, res) => {
  res.send('Home');
});

app.use('/currency', express.static(path.join(__dirname, 'currency.json')));

app.listen(PORT, () => {
  console.log('Server listening at port ', PORT);
});
