import React , {Component} from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import All from './All';
import Add from './Add';
import Detail from './Detail';

const Stack = createStackNavigator();

export default class Home extends Component{
    render(){
        return(
            <NavigationContainer>
            <Stack.Navigator initialRouteName='All'>
                <Stack.Screen name='All' options={{ headerShown: false}} component={All}/>
                <Stack.Screen name='Detail' options={{ headerShown: false }} component={Detail} />
                <Stack.Screen name='Add' options={{ headerShown: false }} component={Add} />
            </Stack.Navigator>
            </NavigationContainer>
        );
    }
}