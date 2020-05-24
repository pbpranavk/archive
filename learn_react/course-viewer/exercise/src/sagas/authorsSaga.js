import { takeEvery, put, call } from "redux-saga/effects";
import { getAuthors } from "../api/authorApi";
import { addAuthorsFromApiToStore } from "../actions/actionCreators";
import "babel-polyfill";
export function* workerAuthorsLoad() {
  const authors = yield call(getAuthors);
  for (let i = 0; i < authors.length; i++) {
    yield put(addAuthorsFromApiToStore(authors[i]));
  }
}

export default function* watcherAuthorsLoad() {
  yield takeEvery("LOAD_AUTHORS", workerAuthorsLoad);
}
