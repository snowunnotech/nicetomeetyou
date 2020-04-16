import 'react-native-gesture-handler';
import React, { Component } from 'react';
import { Provider, useSelector } from 'react-redux';
import { createStore, applyMiddleware, combineReducers } from 'redux';
import { View,Text,Button, } from 'react-native';
import Home from './src/Home.js';

import itemApp from './redux/reducer.js'


//store -> globolized state

//action -> describe what you gonna do
//       -> function that return object
//       -> loaditem
// const loadItem = () => {
//     return{
//         type: 'SCROLL_UP',//下方更新
//     }
// }
// const stayHere = () => {
//     return{
//         type: 'SCROLL_DOWN',
//     }
// }
//reducer -> check which action you did
//        -> how your action transform the state to the next state
//        -> (init)
// const bookLoading = (state = true, action ) => {
//     switch(action.type){
//         case 'SCROLL_UP':
//             return state = true;
//         case 'SCROLL_DOWN':
//             return state = false;
//     }
// }

// let store = createStore(bookLoading);
//display it in the console
// store.subscribe(()=>{
//   console.log(store.getState()) 
// })

//dispatch
// store.dispatch(stayHere());



export default class App extends Component {
  
  render() {
    const store = createStore(itemApp);
    return (
        <Provider store={store}>
        <View style={{flex:1}}>
            <Home />
            </View>
        </Provider>
    );
  }
}