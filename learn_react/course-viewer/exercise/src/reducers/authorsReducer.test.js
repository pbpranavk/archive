import authorsReducer from "./authors";
import {fakeState} from "./fakeStore";

test("Should'nt manipulate when unknown type is passed", () => {
  const newState = authorsReducer(fakeState, { type: "UNRECOGNIZED_ACTIONS" });
  expect(newState).toBe(fakeState);
});

test("Should update when authors api succeds", () => {
  let newAuthor = {
    id: 1,
    name: "Pranav Kumar"
  };
  const newState = authorsReducer(fakeState.authors, {
    type: "ADD_AUTHORS",
    data: newAuthor
  });
  expect(newState).toContainEqual(newAuthor);
});
