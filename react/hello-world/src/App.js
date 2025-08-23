import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Greet from './components/Greet';
import Welcome from './components/Welcome';
import Hello from './components/Hello';

function App() {
  return (
    <div className="App">
      <Greet name="bob" nickname="bobby">
        <h2>This children props.</h2>
        <button>Action</button>
      </Greet>
      <Welcome name="bob" nickname="bobby"/>
      {/* <Hello /> */}
    </div>
  );
}

export default App;
