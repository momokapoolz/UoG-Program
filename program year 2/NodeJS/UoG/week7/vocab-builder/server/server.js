const fs = require('fs') //file system - library of nodejs
const express = require('express')
const port = 3004
const app = express()

app.listen(port, ()=>{
    console.log(`Server is running on port ${port}`)
})

app.get("/", (req,res)=>{

    //read file html using fs(file system)
    fs.readFile("views/index.html", (err, data) =>{ 
        if ((!err)){
            res.writeHead(200, {'Content-Type': 'text/html'})
            res.write(data)
            res.end()
        } else{
            res.writeHead(404, {'Content-Type': 'text/html'})
            res.write("<h1>404</h1><p>Page not found</p>")
            res.end()
        }
    })
})


app.get("/login", (req,res)=>{
    res.send("Login")
})

app.get("/admin", (req,res)=>{
    res.send("Admin")
})