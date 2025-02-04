try {
  decodeURI('http%test')
  console.log('Success!')
} catch(e) {
  console.error(`${e.name}: ${e.message}`)

} finally {
  console.log('The operation (and any error handling) is complete.')
}