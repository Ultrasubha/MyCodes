import React, { Component } from 'react'

export default class ShouldComponentUpdate extends Component {
    constructor(props) {
        super(props);
        this.state={
            firstName: "Subhadeep",
            day:1
        }
    }
    shouldComponentUpdate(nextProps, nextState) {
        console.log(nextProps, nextState)
        if(nextState.day >=17) return false;
        return true;
    }

    componentDidUpdate(prevProps, prevState) {
        console.log(prevProps, prevState)
        if(prevState.day >=15) document.getElementById('field').innerHTML="<h1>Hey, Stop.That's enough.</h1>";
    }
    update = ()=>{
        this.setState({day:this.state.day+1});
    }
  render() {
    return (
      <div id="field">Hits :{this.state.day}
      <button onClick={this.update}>Hit me if you can!</button>
      </div>
    )
  }
}
