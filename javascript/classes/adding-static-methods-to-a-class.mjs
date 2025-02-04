class Book {
  /**
   * Book constructor
   * @param {string} isbn 
   */
  constructor(isbn) {
    this.isbn = isbn
  }

  static isEqual(book, otherBook) {
    if(book instanceof Book && otherBook instanceof Book) {
      return book.isbn.replace(/-/g, '') === otherBook.isbn.replaceAll('-', '')
    }
    return false
  }

  static get isbnPrefix() {
    return '978-1'
  }
}
