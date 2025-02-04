const address = {
  country:'Australia',
  city: 'Sydney',
  streetNum: '412',
  streetName: 'Worcestire Blvd',

}

console.log('streetNum' in address)
console.log('toString' in address)

console.log(address.hasOwnProperty('streetNum'))
console.log(address.hasOwnProperty('toString'))
