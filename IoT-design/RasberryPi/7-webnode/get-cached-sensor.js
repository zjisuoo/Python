const getSensorReadings = require('./get-sensor')

const cache = {
    temperature : 0, humidity: 0
}

setInterval(() => {
    getSensorReadings((err, temperature, humidity) => {
        if(err){
            return console.error(err)
        }
        cache.temperature = temperature
        cache.humidity = humidity
    })
}, 2000)

module.exports.getTemperature = () => cache.temperature
module.exports.getHumidity = () => cache.humidity