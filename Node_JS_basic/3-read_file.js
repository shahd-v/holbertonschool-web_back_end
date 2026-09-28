const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (error, content) => {
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const students = content.trim().split('\n').slice(1)
        .filter((line) => line.length > 0)
        .map((line) => line.split(','));
      const fields = {};

      students.forEach((student) => {
        const field = student[3];
        if (!fields[field]) fields[field] = [];
        fields[field].push(student[0]);
      });

      const lines = [`Number of students: ${students.length}`];
      Object.keys(fields).forEach((field) => {
        lines.push(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
      });
      resolve(lines.join('\n'));
    });
  });
}

module.exports = countStudents;
