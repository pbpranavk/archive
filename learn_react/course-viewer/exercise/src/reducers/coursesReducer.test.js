import coursesReducer from "./courses";
import {fakeState} from "./fakeStore";

test("Should'nt manipulate when unknown type is passed", () => {
  const newState = coursesReducer(fakeState, { type: "UNRECOGNIZED_ACTIONS" });
  expect(newState).toBe(fakeState);
});

test("Should update when courses api is success", () => {
  let newCourse = {
    id: 2,
    title: "Securing React Apps with Auth012",
    slug: "Securing-React-Apps-with-Auth012",
    authorId: "2",
    category: "JavaScript2"
  };
  const newState = coursesReducer(fakeState.courses, {
    type: "ADD_COURSE",
    data: newCourse
  });
  expect(newState).toBe(newCourse);
});

test("Should remove course ", () => {
  let newState = coursesReducer(fakeState.courses, { type: "REMOVE_COURSES" });
  expect(newState).toEqual([]);
});
