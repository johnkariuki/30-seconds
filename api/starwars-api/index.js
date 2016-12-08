const app = require('express')();
const swapi = require('./starwars');
const PORT = 3000;

app.get('/data/:limit/:element/:category/:key', (req, res) => {
  swapi.data(req.params.limit, req.params.element, req.params.category, req.params.key)
    .then(data  => res.status(200).json(data));
});
app.listen(PORT, () => {
  console.log('magic happens on port ', PORT);
});
