import React from 'react'
import FullName from './FullName'

export default function section(props) {
  return (
    <div>
      <FullName fname={props.fname} lname={props.lname} /> Pleased to meet you.
    </div>
  )
}
