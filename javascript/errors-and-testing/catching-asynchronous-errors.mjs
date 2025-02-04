const xhr = new XMLHttpRequest()

xhr.open('GET', 'http://noserver')

xhr.onerror = ev => {
  console.log(ev.type)
}

try {
  xhr.send()
} catch(e) {
  console.error(`${e.name}`)
}
