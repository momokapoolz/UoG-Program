const http = require('http');
const express = require('express')

const app = express()


const server = http.createServer((request,respone) =>{
    respone.write("HELLO");
    respone.write("MY NAME IS");
    respone.write("LGB");

    respone.end(); //must have this
})

app.get("/student", (request, respone)=>{
    respone.send("THIS IS STUDENT ROUTE")
})

server.listen(3068, () =>{
    console.log("server is running on port 3068");
});