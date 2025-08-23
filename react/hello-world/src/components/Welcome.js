import React, { Component } from "react";

class Welcome extends Component {
    render() {
        return (
            <div>
                <h1>class component</h1>
                <p>Welcome {this.props.name}</p>
            </div>
        )
    }
}

export default Welcome;