import * as cheerio from 'cheerio'

(async ()=>{
  try {
    const res = await fetch('https://movie.douban.com')
    const body = await res.text()
    const $ = cheerio.load(body)

    $('.screening-bd img').each((i, el)=>{
      console.log(el.attribs['alt'])
    })
    
  } catch(e) {
    console.error(`error: ${e.message}`)
  }

})()

