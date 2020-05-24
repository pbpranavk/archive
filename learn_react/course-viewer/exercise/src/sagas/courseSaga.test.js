import { runSaga } from "redux-saga";
import {
  addCourseFromApiToStore,
  loadCourses
} from "../actions/actionCreators";
import {
  workerCourseLoad,
  workerDeleteCourse,
  workerCourseUpdate
} from "./courseSaga";

import * as api from "../api/courseApi";

test("should load courses and handle them in case of success", async () => {
  const dispatchedActions = [];
  const mockedCourses = ["abc", "div"];
  api.getCourses = jest.fn(() => Promise.resolve(mockedCourses));
  const fakeStore = {
    dispatch: action => dispatchedActions.push(action)
  };

  await runSaga(fakeStore, workerCourseLoad).done;

  expect(api.getCourses.mock.calls.length).toBe(1);
  expect(dispatchedActions).toContainEqual(
    addCourseFromApiToStore(mockedCourses)
  );
});

test("should delete courses and handle them in case of success", async () => {
  const dispatchedActions = [];
  const mockedCourses = ["abc", "div"];
  api.deleteCourse = jest.fn(id => Promise.resolve({}));
  const fakeStore = {
    dispatch: action => dispatchedActions.push(action)
  };

  await runSaga(fakeStore, workerDeleteCourse, 1).done;

  expect(api.getCourses.mock.calls.length).toBe(1);
  expect(dispatchedActions).toContainEqual(loadCourses());
});

test("should update courses and handle them in case of success", async () => {
  const dispatchedActions = [];
  const mockedCourse = {
    id: 5,
    title: "Securing React Apps with Auth012",
    slug: "Securing-React-Apps-with-Auth012",
    authorId: "2",
    category: "JavaScript2"
  };
  api.saveCourse = jest.fn(course => Promise.resolve(course));
  const fakeStore = {
    dispatch: action => dispatchedActions.push(action)
  };

  await runSaga(fakeStore, workerCourseUpdate, mockedCourse).done;

  expect(api.getCourses.mock.calls.length).toBe(1);
  expect(dispatchedActions).toContainEqual(loadCourses());
});
