class Person {
  constructor(dataOfBirth) {
    this.dataOfBirth = new Date(dataOfBirth)
  }

  get age() {
    if(this.dataOfBirth instanceof Date) {
      const today = new Date()
      let age = today.getFullYear() - this.dataOfBirth.getFullYear()

      return age
    }
  }
}

const me = new Person('1997-02-22')

console.log(me.age)

