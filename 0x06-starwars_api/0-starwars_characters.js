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

  // Fetch and print each character's name in the order provided
  characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(`Error: Unable to fetch character data for URL ${characterUrl}`);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
