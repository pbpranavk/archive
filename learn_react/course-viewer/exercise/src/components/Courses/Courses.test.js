import React from "react";
import renderer from "react-test-renderer";
import { mapStateToProps, mapDispatchToProps, Courses } from "./Courses";
import { BrowserRouter } from "react-router-dom";

jest.mock('../CourseItem/CourseItem', () => 'CourseItem')

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

test("Testing the courses page", () => {
  expect(mapStateToProps(fakeStore).authors.length).toEqual(1);
  const dispatch = jest.fn();

   mapDispatchToProps(dispatch).addCoursestoStore();
   expect(dispatch.mock.calls[0][0]).toEqual({ type: 'LOAD_COURSES'});

});

test("Testing the courses page", () => {
    expect(mapStateToProps(fakeStore).authors.length).toEqual(1);
    const dispatch = jest.fn();
     mapDispatchToProps(dispatch).addAuthorsToStore();
     expect(dispatch.mock.calls[0][0]).toEqual({ type: 'LOAD_AUTHORS'});

  });

  test("Testing the courses page", () => {
    let newCourse = {
      id: 2,
      title: "Securing React Apps with Auth012",
      slug: "Securing-React-Apps-with-Auth012",
      authorId: "2",
      category: "JavaScript2"
    };
    expect(mapStateToProps(fakeStore).authors.length).toEqual(1);
    const dispatch = jest.fn();
    mapDispatchToProps(dispatch).addCourseToStoreForEditing(newCourse);
    expect(dispatch.mock.calls[0][0]).toEqual({ type: 'ADD_EDITABLE_COURSE', data: newCourse});

  });


 test("Protecting against regression issues.....", () => {
   let tree = renderer.create(
     <BrowserRouter>
       <Courses courses={fakeStore.courses} authors={fakeStore.authors} />
     </BrowserRouter>
  ).toJSON();

   expect(tree).toMatchSnapshot();

 });
