import React, { Component } from 'react';
import {
    View,
    Text,
    Button,
    StyleSheet,
    TextInput,
    Alert,
} from 'react-native';
import {
    Container,
    Header,
    Left,
    Right,
    Body,
    Title,
} from 'native-base';
//import { Input } from 'react-native-elements';
export default class Add extends Component {
    constructor(props) {
        super(props);
        this.state = {
            author: '',
            createAt: '',
            content: '',
        }
    }
    InsertDataToServer = () => {
        const { author } = this.state;
        const { createAt } = this.state;
        const { content } = this.state;

        fetch('http://localhost:3000/add', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({

                author: author,

                createAt: createAt,

                content: content,
            })
        }).then((response) => response.json())
            .then((responseJson) => {
                //Alert.alert(responseJson);
            }).catch((error) => {
                console.error(error);
            });
    }
    render() {
        return (
            <Container style={styles.contain}>
                <Header>
                    <Left>
                        <Button title='Back' onPress={() => {
                            this.props.navigation.goBack();
                        }} />
                    </Left>
                    <Body>
                        <Title>Add New Book</Title>
                    </Body>
                    <Right>
                        <Button title='Save' onPress={() => {
                            //傳送資料到Detail
                            this.props.navigation.navigate('Detail', { author: this.state.author, createAt: this.state.createAt, content: this.state.content });
                            this.InsertDataToServer();
                        }} />
                    </Right>
                </Header>

                <TextInput
                    style={styles.input}
                    placeholder='Author'
                    onChangeText={(author) => { this.setState({ author: author }) }}
                    value={this.state.author}
                />

                <TextInput
                    style={styles.input}
                    placeholder='Created at'
                    onChangeText={createAt => this.setState({ createAt: createAt })}
                    value={this.state.createAt}
                />

                <TextInput
                    style={styles.input2}
                    onChangeText={content => this.setState({ content: content })}
                    value={this.state.content}
                />

            </Container>
        );
    }
}

const styles = StyleSheet.create({
    contain: {
        backgroundColor: 'grey',
    },
    input: {
        height: 50,
        backgroundColor: 'white',
        margin: 15,
        borderRadius: 2,
    },
    input2: {
        height: 200,
        backgroundColor: 'white',
        margin: 15,
        borderRadius: 2,
    },
});