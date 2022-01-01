var mysql = require('mysql');

var DB = require('../config/properties').PROD ? require('../config/properties').DB_PROD : require('../config/properties').DB_LOCAL

var pool = mysql.createPool({
    connectionLimit: 100,
    host: DB.HOST,
    user: DB.USERNAME,
    password: DB.PASSWORD,
    database: DB.SCHEMA,
    port: DB.PORT ? DB.PORT : 3306
});

module.exports = pool;
