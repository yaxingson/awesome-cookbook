const dynamicProperty = 'nickname'
const dynamicPropertyValue = 'The Izz'

const employee = {
  employeeId: 402,
  firstName: 'Lisa',
  lastName: 'Stanecki',
  birthDate: new Date(1996, 2, 10),
  [dynamicProperty]:dynamicPropertyValue,

}

employee.role = 'Manager'
employee['birthPlace'] = {
  country:'Canada',
  city:'Toronto'
}

console.log(employee)

