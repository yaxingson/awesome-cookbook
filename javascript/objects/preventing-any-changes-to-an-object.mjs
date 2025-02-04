const customer = {
  firstName: 'Josephine',
  lastName: 'Stanecki'
}

Object.freeze(customer)

// customer.firstName = 'Joe'
// customer.email = ''

console.log(customer)

delete customer.lastName

console.log(customer)


