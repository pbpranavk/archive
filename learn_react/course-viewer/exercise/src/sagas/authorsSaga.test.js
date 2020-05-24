import { runSaga } from "redux-saga";
import { addAuthorsFromApiToStore } from "../actions/actionCreators";
import { workerAuthorsLoad } from "./authorsSaga";
import * as api from "../api/authorApi";

test("should load authors and handle them in case of success", async () => {
  const dispatchedActions = [];
  const mockedAuthors = ["abc", "div"];
  api.getAuthors = jest.fn(() => Promise.resolve(mockedAuthors));
  const fakeStore = {
    dispatch: action => dispatchedActions.push(action)
  };

  await runSaga(fakeStore, workerAuthorsLoad).done;

  expect(api.getAuthors.mock.calls.length).toBe(1);
  expect(dispatchedActions).toContainEqual(
    addAuthorsFromApiToStore(mockedAuthors[0])
  );
});
