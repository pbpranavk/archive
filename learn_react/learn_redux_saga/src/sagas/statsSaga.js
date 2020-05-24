import { take, fork, put, call } from "redux-saga/effects";
import { IMAGES } from "../constants";
import { loadImageStats, setImageStats, setImageStatsError } from "../actions"
import { fetchImageStats } from "../api/index";
import { delay } from "redux-saga";

function* handleStatsRequest(id) {
    for (let i = 0; i < 3; i++) {
        try {
            yield put(loadImageStats(id));
            const res = yield call(fetchImageStats, id);
            yield delay(10000);
            yield put(setImageStats(id, res.downloads.total));
            return true;
        } catch (err) { }
    }
    yield put(setImageStatsError(id));
}


export default function* watchStatsRequest() {
    while (true) {
        const { images } = yield take(IMAGES.LOAD_SUCCESS);
        for (let i = 0; i < images.length; i++) {
            yield fork(handleStatsRequest, images[i].id)
        }
    }
}