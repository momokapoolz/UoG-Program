//1. declare HTTP module
const http = require('http');
//2.declare hosr server
const host = 'localhost'
//3. declare port number
const PORT = 3002

//4.create web server
const server = http.createServer((req, res) => {
    //set content type
    res.setHeader("content type")

    res.write("adu")

    res.end()
})

//5. run server - listen
server.listen(PORT, () =>{
    console.log(`server is running on ${PORT}`);
})