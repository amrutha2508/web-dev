import React from 'react';

// function Greet(){
//     return <h1>Hello Amrutha</h1>
// }

const Greet = (props) => {
    return(
        <div>
            <h1>Greetings {props.name} a.k.a {props.nickname}</h1>
            <p>first child {props.children[0]}</p>
            <p>second child {props.children[1]}</p>
        </div>
    )

    
}


export default Greet;