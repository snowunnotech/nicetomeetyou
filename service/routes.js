const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql');
var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "zaqxsw123"
});

con.connect(function (err) {
    if (err) throw err;
    console.log("Connected!");
});

const app = express();

app.get('/users', function (req, res) {
    con.query('SELECT * FROM ddd.book_listing', function (error, results, fields) {
        if (error) throw error;
        res.send(results)
    });
});
//刪除資料
app.post('/delete', function (req, res) {
    req.on('data', function (data) {
        console.log(data.toString());
        let data1 = data.toString();
        let data2 = JSON.parse(data1);
        console.log(data2.author)
        let sql = "DELETE FROM ddd.book_listing WHERE id=" + data2.id
        con.query(sql, function (error, results, fields) {
            if (error) throw error;
            res.send(results)
        });
    })
});

//加資料
app.post('/add', function (req, res) {
    req.on('data', function (data) {
        console.log(data.toString());
        let data1 = data.toString();
        let data2 = JSON.parse(data1);
        console.log(data2.author)
        let sql = "INSERT INTO ddd.book_listing (author, time, content) VALUES ('" + data2.author + "','" + data2.createAt + "','" + data2.content + "')"
        con.query(sql, function (error, results, fields) {
            if (error) throw error;
            res.send(results)
        });
    });
});

app.listen(3000, () => {
    console.log('Go to http://localhost:3000/ so you can see the data.');
});