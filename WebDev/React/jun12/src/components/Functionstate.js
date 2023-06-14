import React, { useState } from 'react'
import './stl.css'

export default function Functionstate() {
    const [cnt, setCnt] = useState(0)
    const [color, setColor] = useState("light")
    const addOne = ()=>{
        setCnt(cnt+1)
    }

    const multFive = ()=>{
        setCnt(cnt*5)
    }

    const divideFive = ()=>{
        setCnt(cnt/5)
    }

    const changeColor = ()=>{
        {color==="dark"?setColor("light"):setColor("dark")}
    }
console.log(color)
  return (
    <div className={color}>
        <hr />
        <b>{cnt}</b>
        <button onClick={()=>addOne()}>Add</button>
        <button onClick={()=>multFive()}>Multiply 5</button>
        <button onClick={()=>divideFive()}>Divide 5</button>
        <br />
        <button onClick={()=>changeColor()}>Dark/Light</button>
        <hr />
    </div>
  )
}