/*
import React, { Component, useState, useContext } from "react";

import {LineChart, BarChart, Bar, Line, YAxis, CartesianGrid, XAxis, Label} from 'recharts';
const userItems = [
  {
    id: 1,
    name: "Dustin",
    last_name: "McRorie",
  },
  {
    id: 2,
    name: "Mike",
    last_name: "Sandare",
  },
  {
    id: 3,
    name: "Jeff",
    last_name: "Winger",
  },
  {
    id: 4,
    name: "Dank",
    last_name: "Sinatra",
  }
];
class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      viewDustins: "Brosef",
      userItems: userItems,
      count: 3,
    };
  }
  displayCompleted = status => {
    if (status) {
      return this.setState({ viewDustins: "Dustin" });
    }
    return this.setState({ viewDustins: "Brosef" });
  };
  renderTabList = () => {
    return (
      <div className="my-5 tab-list">
        <span
          onClick={() => this.displayCompleted(true)}
          className={this.state.viewCompleted ? "active" : ""}
        >
          complete
        </span>
        <button
          onClick={() => this.setState({count: 5})}//this.displayCompleted(false)}
          className={this.state.viewCompleted ? "" : "active"}
        >
          Increment
        </button>
      </div>
    );
  };
  renderItems = () => {
    const { viewCompleted } = this.state;
    const newItems = this.state.userItems.filter(
      item => true
    );
    return newItems.map(item => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className={`todo-title mr-2 ${
            this.state.viewCompleted ? "completed-todo" : ""
          }`}
          title={item.name}
        >
          {item.name}
        </span>
        <span>
          {this.state.count}
          <button className="btn btn-secondary mr-2"> Edit </button>
          <button className="btn btn-danger">Delete </button>
        </span>
      </li>
    ));
  };
  render() {
    return (
      <main className="content">        
        <h1 className="text-white text-uppercase text-center my-4">Todo app</h1>
        <div className="row ">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="">
                <button className="btn btn-primary">Add task</button>

              </div>
              {this.renderTabList()}
              <ul className="list-group list-group-flush">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
      </main>
    );
  }
}
export default App;
*/

import React, { Component } from 'react'

import Recharts from 'Recharts'

//import defaultStyleOptions from './defaultStyleOptions'

const data = [
  { name: 'Page A', uv: 4000, pv: 2400, amt: 2400 },
  { name: 'Page B', uv: 3000, pv: 1398, amt: 2210 },
  { name: 'Page C', uv: 2000, pv: 9800, amt: 2290 },
  { name: 'Page D', uv: 2780, pv: 3908, amt: 2000 },
  { name: 'Page E', uv: 1890, pv: 4800, amt: 2181 },
  { name: 'Page F', uv: 2390, pv: 3800, amt: 2500 },
  { name: 'Page G', uv: 3490, pv: 4300, amt: 2100 }
];

const options = {
  //...defaultStyleOptions,
  series: {
    _type: 'area',
    fill: 'rgba(97, 125, 233, 0.6)',
    stroke: '#617DE9',
    type: 'monotone',
    label: true
  }
}

const AreaChart = () => (
  <Recharts chart={{ options, data}} />
)

export default AreaChart