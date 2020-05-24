import React from "react";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import "./Course.css";
import { updateCourse } from "../../actions/actionCreators";

export class Course extends React.Component {
  constructor(props) {
    super(props);
    this.titleInput = React.createRef();
    this.categoryInput = React.createRef();
    this.authorInput = React.createRef();
  }

  slugify(url) {
    let wordsInURL = url.split(" ");
    let slugifiedURL = wordsInURL.join("-");
    return slugifiedURL;
  }
  updateCourses(e) {
    e.preventDefault();
    const formData = {};
    for (const field in this.refs) {
      formData[field] = this.refs[field].value;
    }
    let course;
    let { fromEdit, editCourse } = this.props;
    fromEdit ? (course = editCourse[0]) : (course = {});
    course.title = formData["title"];
    course.category = formData["category"];
    course.authorId = formData["author"];
    course.slug = this.slugify(course.title);
    this.props.updateCourse(course);
    this.props.history.push("/courses");
  }
  render() {
    let { authors, fromEdit, editCourse } = this.props;
    let isFromEdit = /true/i.test(fromEdit);
    return (
      <div className="create-course">
        {isFromEdit ? <h2>Edit Course</h2> : <h2>Add Course</h2>}
        <form onSubmit={this.updateCourses.bind(this)}>
          <p>Title</p>
          {isFromEdit ? (
            <input type="text" ref="title" defaultValue={editCourse[0].title} />
          ) : (
            <input type="text" ref="title" />
          )}
          <p>Author</p>
          {isFromEdit ? (
            <select
              id="authorDropdown"
              ref="author"
              defaultValue={editCourse[0].authorId}
            >
              {authors.map((author, id) => (
                <option key={author.id} value={author.id}>
                  {author.name}
                </option>
              ))}
            </select>
          ) : (
            <select id="authorDropdown" ref="author">
              <option key="sel" value="">
                Select an author
              </option>
              {authors.map((author, id) => (
                <option key={author.id} value={author.id}>
                  {author.name}
                </option>
              ))}
            </select>
          )}
          <p>Category</p>
          {isFromEdit ? (
            <input
              type="text"
              ref="category"
              defaultValue={editCourse[0].category}
            />
          ) : (
            <input type="text" ref="category" />
          )}
          <button type="submit">Save</button>
        </form>
      </div>
    );
  }
}

export function mapStateToProps({ courses, authors, editCourse }) {
  return {
    courses,
    authors,
    editCourse
  };
}

export const mapDispatchToPtops = dispatch => ({
  updateCourse: course => {
    dispatch(updateCourse(course));
  }
});

export default withRouter(
  connect(
    mapStateToProps,
    mapDispatchToPtops
  )(Course)
);
