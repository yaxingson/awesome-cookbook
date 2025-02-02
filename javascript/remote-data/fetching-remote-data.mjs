import fs from 'node:fs'
import { Readable } from 'node:stream'

async function fetchWebPage() {
  const res = await fetch('https://www.oreilly.com/')
  const body = await res.text()
  console.log(body)
}

async function fetchApiData() {
  const res = await fetch('https://swapi.dev/api/people/1')
  const data = await res.json()
  console.log(data)
}

async function downloadImage() {
  const res = await fetch('https://cdn.oreillystatic.com/images/sitewide-headers/oreilly_logo_mark_red.svg')
  const dest = fs.createWriteStream('downloads/oreilly_logo.svg')
  Readable.fromWeb(res.body).pipe(dest)
}

(async ()=>{
  await fetchWebPage()
  await fetchApiData()
  await downloadImage()

})()
