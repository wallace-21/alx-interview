#!/usr/bin/node

const request = require('request');

// Star Wars API base URL (template)
const baseUrl = 'https://swapi.dev/api/films/';

// Movie ID from command-line argument
const movieId = parseInt(process.argv[2]);

// Construct the URL for fetching movie data
const movieUrl = `${baseUrl}${movieId}/`;

// Fetch movie data
request(movieUrl, (error, response, body) => {
  if (error) {
    console.error('Error: Unable to fetch movie data');
    process.exit(1);
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters || [];
  const characterRequests = characters.map(characterUrl => new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(`Error: Unable to fetch character data for URL ${characterUrl}`);
      } else {
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      }
    });
  }));

  Promise.all(characterRequests)
    .then(names => {
      names.forEach(name => console.log(name));
    })
    .catch(error => {
      console.error(error);
      process.exit(1);
    });
});

