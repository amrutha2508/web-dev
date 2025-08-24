import React, { Component } from "react";

// ways to bind the "this" to eventHandlers
// 1. use bind() in render with eventHandler
// 2. using arrow functions in render method
// 3. 

class EventBind extends Component{
    // to create state properties user constructor 
    constructor(props){
        super(props)
        this.state = {
            message: 'Hello'
        }
        // this.clickHandler = this.clickHandler.bind(this) // 3rd approach
    }
    // clickHandler(){
    //     this.setState({
    //         message: 'Good Bye'
    //     })
    //     console.log(this)
    // }

    // aproach 4
    clickHandler = () => {
        this.setState({
            message: 'Goodbye'
        })
    }

    render(){
        return(
            <div>
                <div>{this.state.message}</div>
                {/* <button onClick={this.clickHandler.bind(this)}>Click</button> */}
                {/* <button onClick={() => this.clickHandler()}>Click</button> */}
                <button onClick={this.clickHandler}>Click</button>

            </div>
        )
    }
}

export default EventBind;