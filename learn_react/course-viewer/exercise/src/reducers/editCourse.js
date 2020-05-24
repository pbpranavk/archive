function editCourseReducer(state = [], action) {
  switch (action.type) {
    case "ADD_EDITABLE_COURSE":
      return [action.data];
    default:
      return state;
  }
}

export default editCourseReducer;
