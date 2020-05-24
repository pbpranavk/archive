import {createStore, applyMiddleware} from "redux";
import createSagaMiddleware from "redux-saga";
import rootReducer from "./reducers/index";
import rootSaga from "./sagas";
import {composeWithDevTools} from 'redux-devtools-extension/developmentOnly';

const sagaMiddleWare = createSagaMiddleware();
const store = createStore(
    rootReducer,
    composeWithDevTools(
        applyMiddleware(sagaMiddleWare),
    )
    );

sagaMiddleWare.run(rootSaga);

export default store;