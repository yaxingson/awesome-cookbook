import http from 'node:http'
import url from 'node:url'

const PORT = 8124
const HOSTNAME = 'localhost'

http.createServer((req, res)=>{
  res.end('hello,world!')
}).listen(PORT, HOSTNAME, ()=>{
  console.log(`[${new Date().toLocaleString()}] ready on http://${HOSTNAME}:${PORT}/`)
})
