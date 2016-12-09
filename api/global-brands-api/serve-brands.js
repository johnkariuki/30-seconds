/* eslint-disable no-console */

const express = require('express');
const app = express();
const PORT = 3001;
const path = require('path');

app.get('/', (req, res) => {
  res.send('Home');
});

app.use('/brands', express.static(path.join(__dirname, 'brands.json')));

app.listen(PORT, () => {
  console.log('Server listening at port ', PORT);
});
