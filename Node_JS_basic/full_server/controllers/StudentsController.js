import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(request, response) {
    readDatabase(process.argv[2])
      .then((students) => {
        const lines = ['This is the list of our students'];
        Object.keys(students).sort((left, right) => left.localeCompare(right))
          .forEach((field) => {
            const names = students[field];
            lines.push(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
          });
        response.status(200).send(lines.join('\n'));
      })
      .catch(() => response.status(500).send('Cannot load the database'));
  }

  static getAllStudentsByMajor(request, response) {
    const { major } = request.params;
    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(process.argv[2])
      .then((students) => response.status(200).send(`List: ${students[major].join(', ')}`))
      .catch(() => response.status(500).send('Cannot load the database'));
  }
}

export default StudentsController;
