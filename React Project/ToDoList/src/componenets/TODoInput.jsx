import { useState } from "react"

export default function TODoInput(props){
    const{ handleAddTodo,todovalue,setTodoValue }= props
    return(
        <div className="container">
           <input value={todovalue} onChange={(e)=>{
            setTodoValue(e.target.value)
           }} placeholder="here add what ur going to to "></input>
           <button className="AddButton" onClick={() => {
            handleAddTodo(todovalue)
            setTodoValue('')
           }}> Add</button>  
        </div>   
    
    )
}