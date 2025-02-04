import got from 'got'
import dotenv from 'dotenv'

dotenv.config({
  encoding:'utf-8'
})

const env = Object.fromEntries(Object.entries(process.env)
  .filter(item=>item[0].startsWith('REMOTE')))

;(async ()=>{
  try {
    const res = await got(`${env['REMOTE_BASE_URL']}/api/people/2/`)
    console.log(JSON.parse(res.body))
  } catch(e) {
    console.error(`error: ${e.message}`)
  }

})()
