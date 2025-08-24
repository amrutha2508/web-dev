import React from "react";

function ChildComponent(props){
    return(
        <div>
            {/* Here we succsefully called a method in parent component from a button in child component by passing methods as props to child component */}
            {/* <button onClick={props.greetHandler}>Greet Parent</button> */}
            {/* The arrow function format is used inorder to be able to pass parameter from the child to the parent method */}
            <button onClick={()=>props.greetHandler('child')}>Greet Parent</button>
        </div>
    )
}

export default ChildComponent;
