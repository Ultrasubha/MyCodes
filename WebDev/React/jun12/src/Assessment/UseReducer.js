import React, { useReducer } from 'react'

export default function UseReducer() {
    const bgChange = (state, action)=> {
        if(action === "magenta") {
            return{
                backgroundColor: "magentaDiv"
            }
        }
        else if(action === "azure") {
            return{
                backgroundColor: "azureDiv"
            }
        }
        else if(action === "gold") {
            return{
                backgroundColor: "goldDiv"
            }
        }
        else {
            return{
                backgroundColor: "forestgreenDiv"
            }
        }
    }
    const [state, dispatch] = useReducer(bgChange, {backgroundColor: "mainDiv"})
  return (
    <div>
        <div className={state.backgroundColor}></div>
        <button onClick={()=> dispatch("magenta")}>Magenta</button>
        <button onClick={()=> dispatch("azure")}>Azure</button>
        <button onClick={()=> dispatch("gold")}>Gold</button>
        <button onClick={()=> dispatch("green")}>Green</button>

    </div>
  )
}