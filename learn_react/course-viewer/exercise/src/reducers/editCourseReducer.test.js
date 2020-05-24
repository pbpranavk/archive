import editCourse from "./editCourse";
import {fakeState} from "./fakeStore";

test("Should'nt manipulate when unknown type is passed", () => {
  const newState = editCourse(fakeState, { type: "UNRECOGNIZED_ACTIONS" });
  expect(newState).toBe(fakeState);
});

test("Should add editable course to store ", () => {
  let newEditCourse = {
    id: 1,
    title: "Securing React Apps with Auth01",
    slug: "Securing-React-Apps-with-Auth01",
    authorId: "2",
    category: "JavaScript"
  };
  let newState = editCourse(fakeState.editCourse, {
    type: "ADD_EDITABLE_COURSE",
    data: newEditCourse
  });
  expect(newState).toContainEqual(newEditCourse);
});
