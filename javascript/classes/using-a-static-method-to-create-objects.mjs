class Book {
  constructor(title, firstName, lastName) {
    this.title = title
    this.firstName = firstName
    this.lastName = lastName
  }

  static createSequel(title, prevBook) {
    return new Book(title, prevBook.firstName, prevBook.lastName)
  }
}
