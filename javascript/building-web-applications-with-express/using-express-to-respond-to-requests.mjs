import express from 'express'

const PORT = process.env.PORT || '3000'

const app = express()

app.get('/', (req, res)=>{
  res.send('hi,express!')
})

app.listen(PORT, ()=>{
  console.log(`listening at http://localhost:${PORT}`)
})
