const connection = require('../config/database.js')



const getHomepage = (req, res) => {
    connection.connect(function (err) {
        if (err) throw err
        console.log("Connected!");
        connection.query(`SELECT * FROM Users`, function (err, results) {
            if (err) throw err;
            console.log(results);
            return res.render('start.ejs', {listUsers: results}); 
        });
    });
    
}

/*async function getHomepage(data) {
    var sql = "SELECT * FROM Users"
    const results = await connection.promise().query(sql)
    return results[0]
}*/


//render ra file frontend input, phai viet dung thu tu req truoc res sau
const getCreateUser = (req, res) => {
    return res.render('create_user.ejs')
}

//render ra form update
const getUpdateUser = (req, res) => {
    const userID = req.params.id;
    console.log(">>>", req.params, userID)

    connection.connect(function (err) {
        connection.query(`SELECT * FROM Users WHERE id = ?`, [userID], function (err, results) {
            if (err) throw err;
            console.log(results);

            let user = results && results.length > 0 ? results[0] : {};
            return res.render('edit.ejs', {user: user})
        });
    });
}



//create new user
const postCreateUser = (req, res) => {
    let name = req.body.name;
    let city = req.body.city;
    let email = req.body.email;

    console.log(">>> req.body", name, city, email);
    //res.send("tin chuan chua a");

    //var query = `INSERT INTO Users (email, name, city) VALUES (?, ?, ?)`[email, name, city],;

    connection.connect(function (err) {
        if (err) throw err
        console.log("Connected!");
        connection.query(`INSERT INTO Users (email, name, city) VALUES (?, ?, ?)`, [email, name, city], function (err, result) {
            if (err) throw err;
            res.redirect('/');
        });
    });
}


//update user
const UpdateUser = (req, res) => {
    let name = req.body.name;
    let city = req.body.city;
    let email = req.body.email;
    let userId = req.body.userId;

    console.log(">>> req.body", name, city, email, userId);
    //res.send("tin chuan chua a");

    //var query = `INSERT INTO Users (email, name, city) VALUES (?, ?, ?)`[email, name, city],;

    connection.connect(function (err) {
        if (err) throw err
        console.log("Connected!");
        connection.query(`UPDATE Users SET email = ?, city = ?, name = ? WHERE id = ?`, [email, name, city, userId], function (err, result) {
            if (err) throw err;
            //console.log("1 record inserted");
            res.redirect('/');
        });
    });
}


//delete user
const DeleteUser = (req, res) => {
    let userId = req.body.userId;
    connection.connect(function (err) {
        if (err) throw err
        console.log("Connected!");
        connection.query(`DELETE FROM Users WHERE id = ?`, [userId], function (err, result) {
            if (err) throw err;
            //console.log("1 record inserted");
            res.redirect('/');
        });
    });
}



module.exports = {
    getHomepage, getCreateUser, postCreateUser, getUpdateUser, UpdateUser, DeleteUser
}

