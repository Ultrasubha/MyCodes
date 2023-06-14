import React, { Component } from 'react'

export default class Classbased extends Component {
    constructor() {
        super()
        this.state = {
            cnt:0,
            name:"Subhadeep"
        };
    }
    addOne=()=>{
        this.setState({cnt:this.State.cnt+1});
    }
    minusOne=()=>{
        this.setState({cnt:this.State.cnt-1});
    }
    render() {
        return (
        <div>
            <h1>{this.props.name}</h1>
            {this.props.arr.map((item)=>{return <li>{item}</li>})} <hr />
            <button onClick={()=>this.setState({cnt:this.state.cnt -1})}>-</button>
            <b style={{color:'red',fontSize:'x-large'}}>{this.state.cnt}</b>
            <button onClick={()=>this.setState({cnt:this.state.cnt +1})}>+</button>
            <h2>{this.state.name}</h2>
            <button onClick={()=>this.setState({name:"Shirohige"})}>Generate Name</button>
        </div>
        )
    }
}
