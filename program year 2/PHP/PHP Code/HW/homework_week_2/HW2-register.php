<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
    <link rel="stylesheet" href="HW2-register.css">

</head>

<body>
    <h2>Patient Registration</h2>
    <form action="HW2-result.php" method="post">
        <div class="input-group">
            <input type="text" placeholder="First Name" , id="first-name" name="fn">
            <br><br>
            <input type="text" placeholder="Last Name" , id="last-name" name="ln">
            <br><br>
            <input type="date" id="dob" name="dob">
            <br><br>
            <input type="email" placeholder="example@gmail.com" id="email" name="e">
            <br><br>
            <input type="tel" placeholder="Your phone number" id="tel" name="sdt">
            <br><br>
            <button type="submit" id="button" value="send">Register</button>
            <br><br>
        </div>
    </form>
</body>

</html>