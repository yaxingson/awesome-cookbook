class Person {
  constructor(firstName, lastName, dataOfBirth) {
    this.firstName = firstName
    this.lastName = lastName
    this.dataOfBirth = dataOfBirth
  }
}

const person = new Person('Masayoshi', 'Son', new Date(2025, 1, 5))

console.log(person)
