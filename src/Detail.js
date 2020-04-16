import React, { Component } from 'react';
import {
    View,
    Text,
    Button,
    StyleSheet,
} from 'react-native';
import {
    Container,
    Header,
    Left,
    Right,
    Body,
    Title,
} from 'native-base';
export default class Detail extends Component {
    constructor(props){
        super(props);
        this.state={
            author:'',
            content:'',
            createAt:'',
        }
    }
    componentDidMount(){
        const { params: { author,content,createAt } } = this.props.route;
        this.setState({ author ,createAt, content ,});
    }
    componentWillUnmount(){
        this.setState=(state,callback)=>{
            return;
        }
    }
    render() {
        return (
            <Container style={styles.container}>
                <Header>
                    <Left>
                        <Button title='Back' onPress={() => { this.props.navigation.navigate('All'); }} />
                    </Left>
                    <Body>
                        <Title>書名</Title>
                    </Body>
                    <Right>
                        <Button title='Edit' onPress={() => { this.props.navigation.navigate('Add'); }} />
                    </Right>
                </Header>

                <View style={styles.row}>
                    <View style={styles.flex1}>
                        <Text>Author:{this.state.author}</Text>
                    </View>
                    <View style={styles.flex2}>
                        <Text>{this.state.createAt}</Text>
                    </View>
                </View>
                <View style={styles.content}>
                    <Text>{this.state.content}</Text>
                </View>
            </Container>
        );
    }
}

const styles = StyleSheet.create({
    container: {
        backgroundColor: 'grey',
    },
    row: {
        flexDirection: 'row',
    },
    flex1: {
        flex: 1,
        margin: 15,
    },
    flex2: {
        flex:1,
        margin: 15,
        alignItems:'flex-end',
    },
    content: {
        marginLeft: 15,
        marginRight: 15,
    },
});