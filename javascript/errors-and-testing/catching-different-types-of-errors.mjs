try {
  1n + 1
} catch(e) {
  if(e instanceof URIError) {
    console.log('URIError!')
  } else if(e instanceof RangeError) {
    console.log('RangeError!')
  } else if(e instanceof TypeError) {
    console.log('TypeError!')
  } else {
    throw e
  }
}
