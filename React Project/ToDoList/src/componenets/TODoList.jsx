import React from 'react'
import TODoCard from './TODoCard'


export default function TODoList(props) {
    const {todo }=props
  return (
    <div id="listDiv">
        <ul className='main'>
        {todo.map((todo,todoIndex)=>{
            return(
               <TODoCard {...props} key={todoIndex} index ={todoIndex}>
                <p>{todo}</p>
               </TODoCard>
            )
        })}
        </ul>
    </div>
  )
}
