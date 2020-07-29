import React, { Component } from "react";
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
        name: "Frank",
        last_name: "Sinatra",
      }
    ];
    class App extends Component {
      constructor(props) {
        super(props);
        this.state = {
          viewDustins: "Brosef",
          userItems: userItems
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
            <span
              onClick={() => this.displayCompleted(false)}
              className={this.state.viewCompleted ? "" : "active"}
            >
              Incomplete
            </span>
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