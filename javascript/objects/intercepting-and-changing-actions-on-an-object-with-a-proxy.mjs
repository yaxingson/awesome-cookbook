const product = {
  name:'banana',
}

const proxy = new Proxy(product, {
  set(target, property, newValue) {
    target[property] = newValue
  }
})
