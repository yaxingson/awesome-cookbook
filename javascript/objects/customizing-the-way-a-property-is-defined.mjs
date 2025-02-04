const data = {
  rounded: false, 
}

Object.defineProperty(data, 'type', {
  value:'primary',
  enumerable:false,
  writable:true,
})

data.type = 'danger'

console.log(data.type)

for(const key in data) {
  console.log(key)
}

