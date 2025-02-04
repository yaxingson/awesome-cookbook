function isEmptyObj(obj) {
  return Object.keys(obj).length === 0
}

console.log(isEmptyObj({}))
console.log(isEmptyObj({ price:78.21 }))
