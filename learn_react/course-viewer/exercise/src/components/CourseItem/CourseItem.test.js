import React from "react";
import renderer from "react-test-renderer";
import { mapDispatchToPtops, CourseItem } from "./CourseItem";
import { BrowserRouter } from "react-router-dom";

const fakeStore = {
  courses: [
    {
      id: 1,
      title: "Securing React Apps with Auth01",
      slug: "Securing-React-Apps-with-Auth01",
      authorId: "2",
      category: "JavaScript"
    },
    {
        id: 2,
        title: "Securing React Apps with Auth02",
        slug: "Securing-React-Apps-with-Auth02",
        authorId: "2",
        category: "JavaScript2"
      },
      {
        id: 3,
        title: "Securing React Apps with Auth03",
        slug: "Securing-React-Apps-with-Auth03",
        authorId: "2",
        category: "JavaScript3"
      },
      {
        id: 4,
        title: "Securing React Apps with Auth04",
        slug: "Securing-React-Apps-with-Auth04",
        authorId: "2",
        category: "JavaScript4"
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

test("Testing the courseitem", () => {
  let dispatchedActions = [];

  let newCourse = {
    id: 5,
    title: "Securing React Apps with Auth012",
    slug: "Securing-React-Apps-with-Auth012",
    authorId: "2",
    category: "JavaScript2"
  };
  //expect(mapStateToProps(fakeStore).authors.length).toEqual(1);
  const dispatch = jest.fn();
  mapDispatchToPtops(dispatch).deleteCourse(1);
  expect(dispatch.mock.calls[0][0]).toEqual({ type: 'DELETE_COURSE', id: 1});
//   expect(dispatchedActions.length).toEqual(1);
  //expect(fakeStore.courses).toContain(newCourse);
});

test("Protecting against regression issues.....", () => {
  let tree = renderer.create(
      <BrowserRouter>
        <CourseItem course={fakeStore.courses[0]} authors={fakeStore.authors} />
      </BrowserRouter>
  ).toJSON();

  expect(tree).toMatchSnapshot();

});
