import React from "react";
import renderer from "react-test-renderer";
import { BrowserRouter } from "react-router-dom";
import Home from "./Home";

test("Tests for the About component", () => {
        let tree = renderer.create(
            <BrowserRouter>
                <Home />
            </BrowserRouter>
        ).toJSON()

        expect (tree).toMatchSnapshot();
})