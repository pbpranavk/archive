import {questions} from "./questions"

describe("The questions reducer", () => {
    it("should not modify state for unrecognized actions", () => {
        const state = ["foo", "bar"];
        const stateClone = ["foo", "bar"];
        const newState = questions(state, {type:"UNRECOGNIZED_ACTIONS"});

        expect (state).toBe(newState);
    });
    it("should add new questions", () => {
        const state = [{question_id:"Foo"}, {question_id: "bar"}];
        const newQuestion = {question_id:"bar"};
        const newState = questions(state, {type:`FETCHED_QUESTION`, question:newQuestion});

        console.log(newState);

        expect(newState).toContain(newQuestion);
        expect(state).not.toContain(newQuestion);
        expect(newState).toHaveLength(2);
    });
});