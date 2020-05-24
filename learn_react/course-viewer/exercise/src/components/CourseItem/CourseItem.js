import React from "react";
import { Link } from "react-router-dom";
import { connect } from "react-redux";
import { deleteCourseAction } from "../../actions/actionCreators";
import "./CourseItem.css";

export class CourseItem extends React.Component {
  editThisCourse(e) {
    this.props.addCourseToStoreForEditing(this.props.course);
  }
  deleteThisCourse(e) {
    this.props.deleteCourse(this.props.course.id);
  }
  render() {
    let { course, authors } = this.props;
    let authorName = "";
    let path = "/courses/" + course.slug;
    authors.forEach(author => {
      if (author.id == course.authorId) {
        authorName = author.name;
      }
    });
    return (
      <tr>
        <td>
          <button className="watch-button">Watch</button>
        </td>
        <td onClick={this.editThisCourse.bind(this)} className="title">
          <Link to={path}>{course.title}</Link>
        </td>
        <td>{authorName}</td>
        <td>{course.category}</td>
        <td>
          <button onClick={this.deleteThisCourse.bind(this)} className="delete">
            <Link to="/courses">Delete</Link>
          </button>
        </td>
      </tr>
    );
  }
}

export const mapDispatchToPtops = dispatch => ({
  deleteCourse: id => {
    dispatch(deleteCourseAction(id));
  }
});

export default connect(
  null,
  mapDispatchToPtops
)(CourseItem);
