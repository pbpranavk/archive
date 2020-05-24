import React from "react";
import renderer from "react-test-renderer";
import About from "./About";

test("Tests for the About component", () => {
        let tree = renderer.create(
            <About />
        ).toJSON()

        expect (tree).toMatchSnapshot();
})