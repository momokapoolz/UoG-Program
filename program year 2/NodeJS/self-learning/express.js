require('dotenv').config();

const express = require('express')
const app = express()

/* process.env la enviroment variable, them vao de cho cac bien nhu la cong hay
host name co the bi doi khi sang may khac, dung cho cac bien ko co dinh
*/
const port = process.env.PORT || 3001;
const hostname = process.env.HOST_NAME;

const config = require('./src/config/viewEngine');
const router = require('./src/route/web');


//ket noi database mysql
const connection = require('./src/config/database');


//conncetion query
/*connection.query(
    'SELECT * FROM Users',
    function (err, result, fields) {
        console.log(result);
        console.log(fields);
    }
)*/

//config data dc  nhap vao tu form html
app.use(express.json())
app.use(express.urlencoded ({ extended: true}))


//config template engine
config(app);

//static file config
//app.use(express.static(path.join(__dirname, 'public')));
app.use(express.static('public'))

//route hay la dieu huong trang
app.use(router);


app.listen(port, hostname, () => {
    console.log(`Example on port ${port}`)             
})