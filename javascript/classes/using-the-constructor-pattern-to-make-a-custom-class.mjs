function Person(firstName, lastName) {
  this.firstName = firstName
  this.lastName = lastName
}

Person.prototype.learn = function() {}

const newPerson = new Person('Jack', 'Ma')

console.log(newPerson)

