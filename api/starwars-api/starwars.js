const StarWarsAPI = require('star-wars-api');
const swapi = new StarWarsAPI();

let object = {};

function starwars(limit, element, category, key, page = 1, arr = []) {
  return swapi.get('http://swapi.co/api/'+ element + '/' + page + '/')
  .then((res) => {
    arr.push(res[key]);
    if (++page <= limit) {
      return starwars(limit, element, category, key, page, arr);
    }
    return arr;
  })
  .catch(() => {
    if (++page <= limit) {
      return starwars(limit, element, category, key, page, arr);
    }
  });
}

module.exports = {
  data(limit, element, category, key) {
    return starwars(limit, element, category, key).then((res) => {
      object[category] = res;
      // console.log(res);
      return object;
    });
  }
};
