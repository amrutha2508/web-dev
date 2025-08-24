import React, { Component } from 'react';

// using aproach 3 of binding event handlers 
// 1. mention the function to be called in render
// 2. binding the function in the constructor

class Message extends Component {
    
    constructor() {
        super() // a call to the base class constructor from component is being made
        this.state = {
            message: 'Welcome visitor',
            button: 'Subscribe'
        }
        this.changeMessage = this.changeMessage.bind(this)
    }

    changeMessage() {
        // this.setState({
        //     message: "Thank You for Subscribing",
        //     button: "Unsubscribe"
        // })
        this.setState((prevState)=>{
            if(prevState.button ==='UnSubscribe'){
                return {
                    message: 'Welcome visitor',
                    button: 'Subscribe'
                }
            }
            else {
                return {
                    message: "Thank you for subscribing",
                    button: 'UnSubscribe'
                }
            }
        })
    }

    render(){
        return(
            <div>
                <h1>{this.state.message}</h1>
                <button onClick={this.changeMessage}>{this.state.button}</button>
            </div>
        )
    }
}

export default Message;