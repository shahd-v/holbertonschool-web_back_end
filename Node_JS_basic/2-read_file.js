const fs = require('fs');

function countStudents(path) {
  let content;
  try {
    content = fs.readFileSync(path, 'utf8');
  } catch (error) {
    throw new Error('Cannot load the database');
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

  console.log(`Number of students: ${students.length}`);
  Object.keys(fields).forEach((field) => {
    console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
  });
}

module.exports = countStudents;
