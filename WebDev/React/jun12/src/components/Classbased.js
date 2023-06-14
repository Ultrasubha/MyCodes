import React, { Component } from 'react'

export default class Classbased extends Component {
  render() {
    return (
    <div>
        <h1>{this.props.name}</h1>
        {this.props.arr.map((item)=>{return <li>{item}</li>})}
    </div>
    )
  }
}
