const http = require('http')

http.createServer((req, res) =>{
    res.writeHead(200, {'Content-Type': 'application/json'})
    if (req.url == '/'){
        res.write("Welcome")
    } else if (req.url == '/mmb'){
        res.write("mmb")
    } else if (req.url == '/adu'){
        res.write("adu")
    }
}).listen(3003, ()=>{
    console.log(`server is running on ${3003}`)
})

