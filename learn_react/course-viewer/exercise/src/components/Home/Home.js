import React from "react";
import { Link } from "react-router-dom";
import "../../App.css";

class Home extends React.Component {
  render() {
    return (
      <div className="element">
        <div className="jumbotron">
          <h1 className="display-4">Pluralsight Administration</h1>
          <p className="lead">
            React, Redux and React Router for ultra-responsive web apps.
          </p>
          <Link className="btn btn-primary btn-lg" to="/about" role="button">
            Learn more
          </Link>
        </div>
      </div>
    );
  }
}

export default Home;
