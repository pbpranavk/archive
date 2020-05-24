import React from "react";
import renderer from "react-test-renderer";
import { mapStateToProps, mapDispatchToPtops, Course } from "./Course";
import { BrowserRouter } from "react-router-dom";

const fakeStore = {
  courses: [
    {
      id: 1,
      title: "Securing React Apps with Auth01",
      slug: "Securing-React-Apps-with-Auth01",
      authorId: "2",
      category: "JavaScript"
    }
  ],
  authors: [
    {
      id: 1,
      name: "Cory House"
    }
  ],
  editCourse: [
    {
      id: 1,
      title: "Securing React Apps with Auth01",
      slug: "Securing-React-Apps-with-Auth01",
      authorId: "2",
      category: "JavaScript"
    }
  ],
  routing: {
    locationBeforeTransitions: null
  },
};

test("Testing the course page", () => {
  let dispatchedActions = [];

  let newCourse = {
    id: 2,
    title: "Securing React Apps with Auth012",
    slug: "Securing-React-Apps-with-Auth012",
    authorId: "2",
    category: "JavaScript2"
  };
  expect(mapStateToProps(fakeStore).authors.length).toEqual(1);
  const dispatch = jest.fn();
  mapDispatchToPtops(dispatch).updateCourse(newCourse);
  expect(dispatch.mock.calls[0][0]).toEqual({ type: 'UPDATE_COURSE', course: newCourse});
//   expect(dispatchedActions.length).toEqual(1);
  //expect(fakeStore.courses).toContain(newCourse);
});

test("Protecting against regression issues.....", () => {
  let tree = renderer.create(
    <BrowserRouter>
      <Course authors={fakeStore.authors} />
    </BrowserRouter>
  ).toJSON();

  expect(tree).toMatchSnapshot();

});
