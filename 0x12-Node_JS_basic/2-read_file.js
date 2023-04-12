const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const students = data.split('\n').filter(line => line).map(line => line.split(','));
    const fields = {};
    let count = 0;

    students.forEach(student => {
      count++;
      const field = student[3];
      if (!fields[field]) {
        fields[field] = { count: 0, names: [] };
      }
      fields[field].count++;
      fields[field].names.push(student[0]);
    });

    console.log(`Number of students: ${count}`);

    Object.entries(fields).forEach(([field, { count, names }]) => {
      console.log(`Number of students in ${field}: ${count}. List: ${names.join(', ')}`);
    });
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}
