#!/usr/bin/node
const request = require('request');

// Get the episode number from the command line arguments
const episodeNumber = process.argv[2];

// Make a request to the Star Wars API
request(`https://swapi-api.alx-tools.com/api/films/${episodeNumber}`, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Unexpected status code:', response.statusCode);
  } else {
    // Parse the JSON response
    const film = JSON.parse(body);
    // Print the title of the movie
    console.log(film.title);
  }
});
