var express = require('express')
var mongooseDB = require('mongoose')
var app = express()
const bodyParser = require('body-parser');
const route = require('./route')


var port = 3001
mongooseDB.connect('mongodb+srv://legiabao191004:eYC167VhbJYXXfge@cluster-is-cloud-server.wketzko.mongodb.net/')

app.use(bodyParser.json());
app.get('/', (req, res) => {
    res.send('Welcome');
});


app.route("/api", route)

app.listen(port, ()=>{
    console.log("Running on", port)
})
