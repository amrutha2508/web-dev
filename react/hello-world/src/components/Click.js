import React,{Component} from "react";

// react(JSX) events are named using camelCase
// in vanila javascript(JS) use smallcase

// in JSX you pass a function as a {event handler} rather than a "string"

// functional component
function FunctionClick(){
    function clickHandler() {
        console.log('Button Clicked.')
    }
    return(
        <div>
            <button onClick={clickHandler}>Click</button>
        </div>
    )
}

// class component
class ClassClick extends Component {
    clickHandler() {
        console.log('Clicked the button')
    }
    render(){
        return(
            <div>
                <button onClick={this.clickHandler}>Click me</button>
            </div>
        )
    }
}

export {FunctionClick,  ClassClick};
