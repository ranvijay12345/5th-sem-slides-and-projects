var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var mysql = require('mysql');


const bodyParser = require('body-parser');
const cors = require('cors');

var apiRouter = require('./routes/index');

var DB = require('./config/properties').PROD ? require('./config/properties').DB_PROD : require('./config/properties').DB_LOCAL
var app = express();

var connection = mysql.createConnection({
    host: DB.HOST,
    user: DB.USERNAME,
    password: DB.PASSWORD,
    database: DB.SCHEMA,
    port: DB.PORT ? DB.PORT : 3306
})

connection.connect()
connection.query('select * from user', function (err, rows, fields) {
    if (err) throw err
    console.log('Connected: sample user', JSON.stringify(rows))
})

connection.end()

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());

// cross origin resource sharing handler
app.use(cors());

app.use(bodyParser.json());

app.use(express.static(path.join(__dirname, 'public')));

//load expressjs api route
app.use('/api', apiRouter)

//load angular route
// app.get('*', function (req, res) {
//     res.sendFile(path.join(__dirname, 'public/index.html'));
// });

module.exports = app;
