import fs from 'fs';

function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (error, content) => {
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
      resolve(fields);
    });
  });
}

export default readDatabase;
