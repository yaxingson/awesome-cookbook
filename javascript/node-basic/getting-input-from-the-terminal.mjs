import readline from 'node:readline'

const rl = readline.createInterface({
  input:process.stdin,
  output:process.stdout
})

rl.question('Enter your account: ', answer=>{
  console.log(`Account: ${answer}`)
  rl.close()
})