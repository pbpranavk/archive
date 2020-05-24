import { createStore, applyMiddleware, compose } from "redux";
import createSagaMiddleware from "redux-saga";
import rootReducer from "../reducers";

import rootSaga from "../sagas";

const configureStore = () => {
    const sagaMiddleWare = createSagaMiddleware()
    const store = createStore(
        rootReducer,
        compose(
            applyMiddleware(sagaMiddleWare),
            window.__REDUX_DEVTOOLS_EXTENSION__ &&
            window.__REDUX_DEVTOOLS_EXTENSION__(),
        )
    );
    sagaMiddleWare.run(rootSaga);
    return store;
}

export default configureStore;