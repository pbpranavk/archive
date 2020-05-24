import { combineReducers } from "redux";
import { routerReducer } from "react-router-redux";
import coursesReducer from "./courses";
import authorsReducer from "./authors";
import editCourseReducer from "./editCourse";
const rootReducer = combineReducers({
  courses: coursesReducer,
  authors: authorsReducer,
  editCourse: editCourseReducer,
  routing: routerReducer
});

export default rootReducer;
