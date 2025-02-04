const address = {
  country: 'Australia', 
  city: 'Sydney', 
  streetNum: '412',
  streetName: 'Worcestire Blvd',
}

console.log(Object.keys(address))

for(const key in address) {
  console.log(`${key} => ${address[key]}`)
}

