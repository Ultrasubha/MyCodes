import React, { Component } from 'react'

export default class LifeCycleMethods extends Component {
  constructor() {
    super()
    console.log('LifeCycleMethods')
  }

  static getDerivedStateFromProps() {
    console.log('getDerivedStateFromProps')
  }


    render() {
        console.log('render')
    return (
      <div>LifeCycleMethods</div>
    )
  }

  componentDidMount() {
    console.log('componentDidMount()')
  }
}
