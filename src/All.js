import React, { Component } from 'react';
import {
    View,
    Text,
    Button,
    TouchableOpacity,
    StyleSheet,
    FlatList,
    RefreshControl,
} from 'react-native';
import {
    Container,
    Header,
    Left,
    Right,
    Body,
    Title,
} from 'native-base';
import { Icon, } from 'react-native-elements';
import { connect } from 'react-redux';
import * as actionCreators from '../redux/action';
//import itemApp from '../redux/reducer';
import { createStore, } from 'redux';
class All extends Component {
    constructor(props) {
        super(props);
        this.state = {
            arr: [],
        }
    }

    handleItemAdd = () => {
        this.props.hasActivityIndicator();//滑動

        fetch('http://localhost:3000/users')
            .then(function (response) {
                return response.json();
                //console.log(response.json())
            })
            .then(myJson => {
                //console.log(myJson);
                this.props.onItemAdd({
                    myJson
                })
                //console.log(this.props.onItemAdd(myJson).list)
                console.log('===============')
                console.log(this.props.items);
                console.log('===============')
            });
        // this.props.onItemAdd();
        // console.log('=================')
        // console.log( this.props.onItemAdd())

        // console.log(this.props.items)
        // console.log('=================')
    }
    componentDidMount() {
        fetch('http://localhost:3000/users')
            .then(function (response) {
                return response.json();
                //console.log(response.json())
            })
            .then(myJson => {
                //console.log(myJson);
                this.props.onItemAdd({
                    myJson
                })
                //console.log(this.props.onItemAdd(myJson).list)
                // console.log('===============');
                // console.log(this.props.items);
                // console.log('===============');
            });
    }
    //載入更多
    load = () => {
        fetch('http://localhost:3000/users')
            .then(function (response) {
                return response.json();
                //console.log(response.json())
            })
            .then(myJson => {
                //console.log(myJson);
                this.setState({ arr: myJson, });
            });
    }
    delete = (id) => {
        //刪除資料
        fetch('http://localhost:3000/delete', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                id: id,
            })
        }).then((response) => response.json())
            .then((responseJson) => {
                //Alert.alert(responseJson);
            }).catch((error) => {
                console.error(error);
            });
    }
    componentWillUnmount() {
        this.setState = (state, callback) => {
            return;
        }
    }



    Item = (title, author, time, id) => {
        return (
            <View style={styles.itemView}>
                <View>
                    <Icon
                        name='clear'
                        onPress={() => {
                            this.delete(id);
                        }}
                    />
                </View>
                <View>
                    <Text style={styles.title}>{title}</Text>
                </View>
                <View style={styles.item}>
                    <Text style={styles.title}>by {author} {time}</Text>
                </View>
            </View>
        );
    }
    render() {

        return (
            <Container style={styles.container}>
                <Header>
                    <Left />
                    <Body>
                        <Title></Title>
                    </Body>
                    <Right>
                        <Button title='New' onPress={() => { this.props.navigation.navigate('Add'); }} />
                    </Right>
                </Header>
                <FlatList
                    data={this.props.items.myJson}
                    numColumns={2}
                    renderItem={({ item }) => this.Item(item.content, item.author, item.time, item.id)}
                    keyExtractor={item => item.id}
                    refreshControl={
                        <RefreshControl
                            refreshing={this.props.has}
                            onRefresh={() => {
                                console.log('載入資料');
                                this.handleItemAdd();
                            }}
                        />}
                // id -> mySql有auto increment
                />

                {/* //也有下拉刷新載入資料（redux） */}
                <View style={styles.cnt}>
                    <TouchableOpacity style={styles.button}
                        onPress={() => {
                            this.load();
                        }}>
                        <Text style={styles.text}>Load more</Text>
                    </TouchableOpacity>
                </View>
            </Container>
        )
    }
}
const styles = StyleSheet.create({
    container: {
        backgroundColor: 'grey'
    },
    button: {
        alignItems: 'center',
        width: 60 + '%',
        backgroundColor: '#228B22',
        padding: 18,
        marginTop: 20,
        borderRadius: 5,
    },
    text: {
        fontSize: 20,
        color: 'white'
    },
    cnt: {
        alignItems: 'center',
        marginBottom: 15,
    },
    itemView: {
        width: 50 + '%',
        height: 170,
        alignItems: 'center',
        backgroundColor: 'white',
        borderWidth: 15,
        borderColor: 'grey',
    },
    item: {
        flex: 1,
        alignItems: 'center',
        marginTop: 10,
    },

});

const mapStateToProps = store => (
    { items: store.items, has: store.has }
)

export default connect(mapStateToProps, actionCreators)(All)