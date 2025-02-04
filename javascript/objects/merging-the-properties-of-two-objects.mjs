const address = {
  country: 'Australia', 
  city: 'Sydney', 
  streetNum: '412',
  streetName: 'Worcestire Blvd',
}

const customer = {
  firstName: 'Lisa', 
  lastName: 'Stanecki',
}

const customerWithAddress = {...address, ...customer}

console.log(customerWithAddress)
