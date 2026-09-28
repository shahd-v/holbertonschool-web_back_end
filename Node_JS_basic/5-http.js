const http = require('http');
const countStudents = require('./3-read_file');

const app = http.createServer((request, response) => {
  response.statusCode = 200;
  response.setHeader('Content-Type', 'text/plain');

  if (request.url === '/') {
    response.end('Hello Holberton School!');
    return;
  }

  if (request.url === '/students') {
    response.write('This is the list of our students\n');
    countStudents(process.argv[2])
      .then((students) => response.end(students))
      .catch(() => response.end('Cannot load the database'));
  }
});

app.listen(1245);

module.exports = app;
