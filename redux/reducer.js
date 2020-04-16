
import { combineReducers, } from 'redux';


function items(state = [], action) {
    switch (action.type) {
        case 'isRefreshing':
            return action.list
        default:
            return state;
    }
}

function has(state= false, action) {
    switch (action.type) {
        case 'hasActivityIndicator':
            return true;
        default :
            return false
    }
}
//整合reduces
const itemApp = combineReducers({ items, has });

export default itemApp;