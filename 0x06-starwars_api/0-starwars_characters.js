#!/usr/bin/node
const request = require('request');

const requestData = (url) => {
  return new Promise((resolve, reject) => {
    request.get(url, (err, res, body) => {
      if (err || res.statusCode !== 200) {
        reject(new Error(`Request to ${url} failed`));
      }
      const data = JSON.parse(body);
      resolve(data);
    });
  });
};

const printCharacters = (characters) => {
  characters.forEach(character => {
    console.log(character);
  });
};

const fetchFilm = async (filmId) => {
  const baseUrl = 'https://swapi-api.alx-tools.com/api';

  const film = await requestData(`${baseUrl}/films/${filmId}`);

  Promise.all(film.characters.map(async (charUrl) => {
    const char = await requestData(charUrl);
    return char.name;
  })).then(names => {
    printCharacters(names);
  }).catch((error) => {
    console.error(error);
  });
};

fetchFilm(process.argv[2]);
