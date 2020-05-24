import { takeEvery, put, call } from "redux-saga/effects";
import { getCourses, deleteCourse, saveCourse } from "../api/courseApi";
import {
  addCourseFromApiToStore,
  loadCourses
} from "../actions/actionCreators";
import "babel-polyfill";

export function* workerCourseLoad() {
  const courses = yield call(getCourses);
  yield put(addCourseFromApiToStore(courses));
}

export function* workerCourseUpdate(action) {
  const res = yield call(saveCourse, action.course);
  yield put(loadCourses());
}

export function* workerDeleteCourse(action) {
  const res = yield call(deleteCourse, action.id);
  yield put(loadCourses());
}

export default function* watcherCourseLoad() {
  yield takeEvery("LOAD_COURSES", workerCourseLoad);
  yield takeEvery("DELETE_COURSE", workerDeleteCourse);
  yield takeEvery("UPDATE_COURSE", workerCourseUpdate);
}
