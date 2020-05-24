import React from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";

import "../App.css";
import Home from "./Home/Home";
import Courses from "./Courses/Courses";
import About from "./About/About";
import Navbar from "./Navbar";
import GenericNotFound from "./GenericNotFound/GenericNotFound";
import Course from "./Course/Course";

class Main extends React.Component {
  render() {
    return (
      <BrowserRouter {...this.props}>
        <Navbar {...this.props} />
        <Switch>
          <Route exact path="/" component={Home} />
          <Route
            exact
            path="/courses"
            render={props => <Courses {...props} />}
          />
          <Route path="/courses/*" render={() => <Course fromEdit="true" />} />
          <Route exact path="/about" component={About} />
          <Route exact path="/course" component={Course} />
          <Route component={GenericNotFound} />
        </Switch>
      </BrowserRouter>
    );
  }
}

export default Main;
