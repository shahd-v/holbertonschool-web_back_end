const express = require('express');
const countStudents = require('./3-read_file');

const app = express();

app.get('/', (request, response) => {
  response.status(200).send('Hello Holberton School!');
});

app.get('/students', (request, response) => {
  response.write('This is the list of our students\n');
  countStudents(process.argv[2])
    .then((students) => response.status(200).end(students))
    .catch(() => response.status(500).end('Cannot load the database'));
});

app.listen(1245);

module.exports = app;
