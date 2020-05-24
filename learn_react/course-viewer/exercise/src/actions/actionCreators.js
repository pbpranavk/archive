export function addEditableCourse(data) {
  return {
    type: "ADD_EDITABLE_COURSE",
    data: data
  };
}

export function addCourseFromApiToStore(data) {
  return {
    type: "ADD_COURSE",
    data: data
  };
}

export function addAuthorsFromApiToStore(data) {
  return {
    type: "ADD_AUTHORS",
    data: data
  };
}

export function loadCourses() {
  return {
    type: "LOAD_COURSES"
  };
}

export function loadAuthors() {
  return {
    type: "LOAD_AUTHORS"
  };
}

export function updateCourse(course) {
  return {
    type: "UPDATE_COURSE",
    course: course
  };
}

export function deleteCourseAction(id) {
  return {
    type: "DELETE_COURSE",
    id: id
  };
}
