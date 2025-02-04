const factorialize = require('./factorialize')

describe('factorialize function tests', ()=>{
  test('Throw an exception when the arg is less than 0', ()=>{
    expect(jest.fn(()=>factorialize(-1))).toThrow(/positive/)
  })

  test('Throw an exception when the arg is not an integer', ()=>{
    expect(jest.fn(()=>factorialize(20.25))).toThrow(RangeError)
  })
  
  test('0! is 1', ()=>{
    expect(factorialize(0)).toBe(1)
  })

  test('8! is 40320', ()=>{
    expect(factorialize(8)).toBe(40320)
  })
})


