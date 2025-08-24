import React,{Component} from "react";
import ChildComponent from "./ChildComponent";

class ParentComponent extends Component {
    
    constructor(props) {
        super(props)
        this.state = {
            parentName: 'Parent'
        }
        this.greetParent = this.greetParent.bind(this)
    }

    greetParent(childName){
        alert(`Hello ${this.state.parentName} from ${childName}`)
    }

    render(){
        return(
            <div>
                {/* Here we are passing the parent method as a prop to child */}
                <ChildComponent greetHandler={this.greetParent}/>
            </div>
        ) 
    }
}

export default ParentComponent;