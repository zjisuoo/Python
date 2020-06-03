var sensor = require('node-dht-sensor')

sensor.read(11, 4, funcion(err, temperature, humidity) {
    if (!err){
        console.log(
            'temp : ' + temperature.toFixed(1) + 
            ' ' + 
            'humidity : ' + 
            humidity.toFixed(1)
            )
        }
    }
})