import React, { UseEffect, useState } from 'react'
import stl from './componenets/stl.css';

export default function Jokes() {
    const [setup, setSetup] = useState("")
    const [punchline, setPunchline] = useState("")
    const [type, setType] = useState("")

    let generateJoke = async() => {
        try {
            let jokeUrl = await fetch("https://official-joke-api.appspot.com/random_joke")
            let jokeJson = await jokeUrl.json()
            setSetup(jokeJson.setup)
            setPunchline (jokeJson.punchline)
            setType(jokeJson.type)
        }
        catch(error) {console.log(error);}
        UseEffect(() => {generateJoke()}, [])
        return (
            <div>
                <pre className={stl.elem}>
                    <b>Question:</b> <q style="color: rebeccapurple;">{setup}</q> <br />
                    <b>Punchline:</b><i style="color: forestgreen;"> {punchline}</i>
                </pre>
                <h1 className={stl.h1}>Type of joke: {type}</h1>
                <button onClick={generateJoke} className='generateJokeBtn'>Generate Joke</button>
            </div>
        )
    }
}