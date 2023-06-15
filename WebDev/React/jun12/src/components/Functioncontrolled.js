import React from 'react'

export default function Functioncontrolled() {
    const [fname,setFname] = useState("")
    const [lname,setLname] = useState("")
  return (
    <div>
        <form onChange={this.submitHandler}>
        <input type="text" placeholder='FirstName' onChange={(event)=>{this.setState({fname: event.target.value})}} />
        <input type="text" placeholder=':LastName' onChange={(event)=>{this.setState({fname: event.target.value})}} />
        <button type="submit">Submit</button>
        </form>
        <h1>Welcome {this.state.fname}</h1>
        {console.log(this.state.fname)}
    </div>
  )
}
