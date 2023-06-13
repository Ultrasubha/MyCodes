import React from 'react'

var arr=[{name:"Adfar",age:25,skills:["HTML","CSS","JS"]}, {name:"Aman",age:21,skills:["CPP","C#","Python"]}]

export default function Mapping() {
  return (
    <div>
        <table style={{border:"2px solid red"}}>
            <tr>
                {arr[0].map((item,index)=>{
                    return (
                        <th>{item.name}</th>
                    )
                })}
            </tr>
            {/*arr.slice(1).map((item,index)=>{
                return (
                    <tr>
                        <td>{item.name}</td>
                        <td>{item.age}</td>
                        <td>{item.skill.map((item1,index1)=>{
                                return (
                                    <li>{item1}</li>
                                )
                        })}</td>
                    </tr>
            })*/}
        </table>
    </div>
  )
}
