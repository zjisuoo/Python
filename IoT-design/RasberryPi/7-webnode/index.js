const express = require('express')
const path = requir('path')
const app = express()
const getCachedSensorReadings = require('./get-cached-sensor')
const databaseOperations = require('./database-operations')

app.use('/public', express.static(path.join(__dirname, 'public')))

app.get('/temperature', function(req, res){
    res.json({
        value : getCachedSensorReadings.getTemperature().toFixed(1)
    })
})
app.get('/temperature/history', function(req, res){
    databaseOperations.fetchLatestReadings('temperature', 10, (err, results) => {
        if(err){
            console.error(err)
            return res.status(500).end()
        }
        res.json(results.reverse())
    })
})
app.get('/humidity', function(req, res){
    res.json({
        value : getCachedSensorReadings.getHumidity().toFixed(1)
    })
})
app.get('/humidity/history', function(req, res){
    databaseOperations.fetchLatestReadings('humidity', 10, (err, results) => {
        if(err){
            console.error(err)
            return res.status(500).end()
        }
        res.json(results.reverse())
    })
})

app.listen(3000, function(){
    console.log('Server Listening on port 3000')
})