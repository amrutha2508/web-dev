import React, { Component } from "react";

// never modify the state directly, make use of setState
class Counter extends Component{
    // direct usage of this.state without setState only in constructor
    constructor(props) {
        super(props)
        this.state = {
            count: 0
        }
    }
    // Inside your increment function, you log console.log('not callback :', this.state.count) immediately after calling setState.
    // But setState is asynchronous — React batches state updates for performance reasons.
    // So when that log runs, React has not updated this.state.count yet, meaning it still shows the old value (0).
    // setState we let React know it has to rerender the component
    // calls to setState is asynchronous. below the console.log is being called before the state changes.
    // to execute code only after the state changes use callback function as 2nd parameter in setState funciton
    // This callback only runs after React has applied the state updates and re-rendered.
    // Because you call increment five times, React batches all of them together, applies the state updates (+1 each time), and then executes the callback once after all updates are done.
    // Final result → count = 5.
    increment() {
        // this.setState({
        //     count: this.state.count + 1
        // },
        // ()=>{
        //     console.log('Callback value: ', this.state.count)
        // })
        this.setState((prevState)=>({
            count: prevState.count + 1
        }),()=>{
            console.log('Callback value:' , this.state.count)
        })
        console.log('not callback :',this.state.count)
    }
    
    incrementFive() {
        this.increment()
        this.increment()
        this.increment()
        this.increment()
        this.increment()
    }

    render(){
        return(
            <div>
                <div>Count - {this.state.count}</div>
                <button onClick={()=> this.incrementFive()}>Increment</button>
            </div>
        )
    }
}

export default Counter;