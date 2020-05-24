import { all } from "redux-saga/effects";
import courseSaga from "./courseSaga";
import authorsSaga from "./authorsSaga";

function* rootSaga() {
  yield all([courseSaga(), authorsSaga()]);
}

export default rootSaga;
