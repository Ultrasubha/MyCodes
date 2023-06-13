import React from 'react'
import Section from './Section';

export default function About(props) {
  return (
    <div>
        Before I introduce myself, please get aquinted about my friends.
        My friends are {props.dost.map((item)=>{return <li>{item}</li>})}<br />
        My true Alias is {props.death.Alias} and some of my fellow captains in Gotei {props.death.Gotei} are {props.death.SoulReapers.map((item)=>{return <i>{item} | </i>})}
        <Section fname={props.fname} lname={props.lname} />
    </div>
  )
}
