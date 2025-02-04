class Person {
  constructor(firstName, lastName) {
    this.firstName = firstName
    this.lastName = lastName
  }

  toString() {
    return `${this.lastName} ${this.firstName}`
  }
}

const person = new Person('Masayoshi', 'Son')

console.log('' + person)
