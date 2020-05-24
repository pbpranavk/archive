function authorsReducer(state = [], action) {
  switch (action.type) {
    case "ADD_AUTHORS":
      let id = action.data.id;
      let name = action.data.name;
      return [...state, { id: id, name: name }];
    default:
      return state;
  }
}

export default authorsReducer;
