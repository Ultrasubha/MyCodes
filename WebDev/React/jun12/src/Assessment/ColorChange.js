import React, { useState } from 'react'
import "./ColorChange.css"
export default function ColorChange() {
    const [color, setColor] = useState("light")

    const toggle=() => {
        {color==="dark"?setColor("light"):setColor("dark")}
    }
  return (
    <div>
        <div className={color}>Hey</div>
        <button onClick={toggle}>btn1</button>
        <button onClick={toggle}>btn2</button>
        <button onClick={toggle}>btn3</button>
        <button onClick={toggle}>btn4</button>
        <button onClick={toggle}>btn5</button>
    </div>
  )
}
