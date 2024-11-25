const express = require('express')
const app = express()

//1) declare & config "mongoose"
const mongoose = require('mongoose')
const db = "mongodb+srv://lgb:lgb191004@cluster0.ked3o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  //vocab-builder: db name


mongoose.connect(db)
   .then(() => console.log('connect to db succeed !'))
.catch((err) => console.error('connect to db failed ! ' + err))

//2) declare & config "body-parser"
const bodyParser = require('body-parser')
app.use(bodyParser.urlencoded({ extended: true }))
app.use(bodyParser.json())

//3) declare & config CORS
//Note: must declare before any route
const cors = require('cors')
app.use(cors())

//4) declare & register router
const vocabRouter = require('./api/routes/vocabRouter')
vocabRouter(app)

//5) run server by listening port
const port = process.env.PORT || 3000
app.listen(port)
