export default function createReportObject(employeesList) {
    const allEmployees = {};
  
    for (const [departmentName, employees] of Object.entries(employeesList)) {
      allEmployees[departmentName] = [...employees];
    }
  
    return {
      allEmployees: allEmployees,
      getNumberOfDepartments() {
        return Object.keys(allEmployees).length;
      },
    };
  }