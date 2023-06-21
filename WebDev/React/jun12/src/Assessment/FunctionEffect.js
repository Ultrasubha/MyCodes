import React, {useEffect, useState } from 'react'

export default function FunctionEffect() {
    let [count,setCount] = useState(0)
    let [number, setNumber] = useState(5)
    useEffect(()=>{
        console.log("useEffect invoked")
    })
  return (
    <div>
        <hr/>
        <h1>{count}</h1>
        <h1>{number}</h1>
        <button onClick={()=>setCount(count +1)}>Update count</button>
        <button onClick={()=>setCount(number -1)}>Update count</button>
    </div>
  )
}
