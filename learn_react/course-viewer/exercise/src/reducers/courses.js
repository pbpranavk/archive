function coursesReducer(state = [], action) {
  switch (action.type) {
    case "ADD_COURSE":
      return action.data;
    case "REMOVE_COURSES":
      return [];
    default:
      return state;
  }
}

export default coursesReducer;
