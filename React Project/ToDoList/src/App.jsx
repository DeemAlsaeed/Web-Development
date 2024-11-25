import { useState,useEffect } from "react"
import TODoInput from "./componenets/TODoInput"
import TODoList from "./componenets/TODoList"


function App() {
const [todo,setTodo]=useState([])
const[todovalue,setTodoValue]=useState('')

function presistData(newList){
  localStorage.setItem('todo',JSON.stringify({todo:newList}))
}




 function handleAddTodo(newTodo){
  const newTodoList=[...todo,newTodo]
  presistData(newTodoList)
  setTodo(newTodoList)
 }

 function handleDeleteTodo(index){
  const  newTodoList = todo.filter((todo,todoIndex)=>{
    return todoIndex !== index
  })
  setTodo(newTodoList)
  presistData(newTodoList)

 }
 function handleEditTodo(index){
  const valueToBEEdited =todo[index]
  setTodoValue(valueToBEEdited)
  handleDeleteTodo(index)
  
 }
 useEffect(()=>{
  if(!localStorage){
    return
  }
  let localTodo=localStorage.getItem('todo')
  if(!localTodo){
    return 
  }

    localTodo=JSON.parse(localTodo).todo
    setTodo(localTodo)
  
 },[])
  return (
    <>
      <TODoInput     todovalue={todovalue} setTodoValue={setTodoValue}
       handleAddTodo={handleAddTodo}/>
      <TODoList handleEditTodo={handleEditTodo} handleDeleteTodo={handleDeleteTodo} todo={todo}/>
    </>
  )
}

export default App
