#!/usr/bin/node
const axios = require('axios');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

axios.get(url)
  .then((response) => {
    fs.writeFile(filePath, response.data, (err) => {
      if (err) {
        console.error('Error writing to file:', err);
      } else {
        console.log('Data has been successfully written to the file.');
      }
    });
  });
