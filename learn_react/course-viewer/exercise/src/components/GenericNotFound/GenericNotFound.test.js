import React from "react";
import renderer from "react-test-renderer";
import { BrowserRouter } from "react-router-dom";
import GenericNotFound from "./GenericNotFound";

test("Tests for the About component", () => {
        let tree = renderer.create(
            <BrowserRouter>
                <GenericNotFound />
            </BrowserRouter>
        ).toJSON()

        expect (tree).toMatchSnapshot();
})