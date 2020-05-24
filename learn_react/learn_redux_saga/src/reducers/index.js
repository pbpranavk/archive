import { combineReducers } from "redux";

import loadingReucer from "./loadingReducer"
import imagesReducer from "./imagesReducer"
import errorReucer from "./errorReducers"
import pageReducer from "./pageReducer.js"
import statsReducer from "./statsReducer.js"
const rootReducer = combineReducers({
    isLoading: loadingReucer,
    images: imagesReducer,
    error: errorReucer,
    nextPage: pageReducer,
    imageStats: statsReducer,
});

export default rootReducer;