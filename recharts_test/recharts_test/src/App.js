//tutorial site: https://hackernoon.com/how-to-create-and-deploy-a-create-react-app-with-recharts-the-wikiquotes-api-and-a-data-set-1f3a90fccb2d

//Original function App()
/*
import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header> 
    </div>
  );
}*/

//................................................

import React, { Component } from 'react'

const initialReformat = (data) => {
  let temp = {}
  return data.fact.map(row => {
    temp = row.Value
    row = row.dims
    row.Value = temp
    return row
  })
}

const sortDataByYear = data => {
  var sortByYear = {}
  data.forEach( row => {
      if (!sortByYear[row.YEAR]) {
          sortByYear[row.YEAR] = []
          sortByYear[row.YEAR].push(row);
      }else{
          sortByYear[row.YEAR].push(row);
      }
  })
  return sortByYear
}

const finalData = []
var sortByYear = {} //?
var i = 0           //?
for(const year in sortByYear){
  finalData.push({ year })
  sortByYear[year].forEach(obj => {
      if (parseFloat(finalData[i][obj.COUNTRY > 0])){
          finalData[i][obj.COUNTRY] = (finalData[i][obj.COUNTRY] + parseFloat(obj.Value)) / 2
      }
      else finalData[i][obj.COUNTRY] = 
          parseFloat(obj.Value).toFixed(2)
  })
  i++
}

function App(){
  return (
    <div className="App">

    </div>
  );
}

export default App;
