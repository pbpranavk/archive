import React from "react";
import { connect } from "react-redux";
import { Link } from "react-router-dom";

import {
  addEditableCourse,
  loadCourses,
  loadAuthors
} from "../../actions/actionCreators";
import CourseItem from "../CourseItem/CourseItem";
import "../../App.css";
import "./Courses.css";

export class Courses extends React.Component {
  constructor(props) {
    super(props);
    this.textInput = React.createRef();
  }

  componentDidMount() {
    if (this.props.courses.length == 0) this.props.addCoursestoStore();
    if (this.props.authors.length == 0) this.props.addAuthorsToStore();
  }

  render() {
    let courses = this.props.courses;
    return (
      <div className="element">
        <h2>Courses</h2>
        <button className="btn add-course">
          <Link to="/course">Add Course</Link>
        </button>
        <table className="table table-hover">
          <thead>
            <tr>
              <th />
              <th>Title</th>
              <th>Author</th>
              <th>Category</th>
              <th />
            </tr>
          </thead>
          <tbody>
            {courses.map((course, i) => (
              <CourseItem key={course.id} course={course} {...this.props} />
            ))}
          </tbody>
        </table>
      </div>
    );
  }
}

export function mapStateToProps({ courses, authors }) {
  return {
    courses,
    authors
  };
}

export const mapDispatchToProps = dispatch => ({
  addCoursestoStore: () => {
    dispatch(loadCourses());
  },

  addAuthorsToStore: () => {
    dispatch(loadAuthors());
  },

  addCourseToStoreForEditing: course => {
    dispatch(addEditableCourse(course));
  }
});
export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Courses);
