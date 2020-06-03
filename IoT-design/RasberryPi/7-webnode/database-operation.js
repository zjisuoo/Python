const sqlite3 = require('sqlite3')
const path = require('path')
const db = new sqlite3.Database(path.resolve('../test.db'))

const insertReading = (type, reading) => {
    db.run('INSERT INTO ${type} VALUES (datetime('now'), ${reading});')
}
const fetchLatesReadings = (type, limit, callback) => {
    db.all('SELECT * FROM ${type} ORDER BY createAt DESC LIMIT ${limit}', callback)
}

module.exports = {
    insertReading, fetchLatesReadings
}