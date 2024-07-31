#!/usr/bin/node

const request = require('request'); // Added semicolon

// Star Wars API base URL (template)
const baseUrl = 'https://swapi.dev/api/films/'; // Added semicolon

// Movie ID from command-line argument
const movieId = parseInt(process.argv[2]); // Added semicolon

// Construct the URL for fetching movie data
const movieUrl = `${baseUrl}${movieId}/`; // Added semicolon

// Fetch movie data
request(movieUrl, (error, response, body) => {
  if (error) {
    console.error('Error: Unable to fetch movie data'); // Added semicolon
    process.exit(1); // Added semicolon
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters || [];
  const characterRequests = characters.map(characterUrl => new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(new Error(`Error: Unable to fetch character data for URL ${characterUrl}`)); // Added semicolon
      } else {
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      }
    });
  }));

  Promise.all(characterRequests)
    .then(names => {
      names.forEach(name => console.log(name)); // Added semicolon
    })
    .catch(error => {
      console.error(error.message); // Added semicolon
      process.exit(1); // Added semicolon
    });
});
