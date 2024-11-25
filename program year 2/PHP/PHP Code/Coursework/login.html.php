<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <link rel="stylesheet" href="style.css">
    <title><?= $title ?></title>
</head>

<body>
    <div class="p-3 mb-2 bg-info text-white">
        <h1 class="text-center" class="display-1" class="p-3 mb-2 bg-info text-white">Welcome to Stuck Overflow.</h1>
    </div>
    <br>
    <div class="text-center">
        <h1 class="text-info">Login</h1>
    </div>
    <div class="d-flex justify-content-center">
        <form action="" method="post">
            <div class="form-group">
                <label for="exampleInputUsername1">Username:</label>
                <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter username" name="username" required minlength=3>
                <small id="note" class="form-text text-muted">Please enter a valid username</small>
            </div>
            <div class="form-group">
                <label for="exampleInputPassword1">Password</label>
                <input type="password" class="form-control" id="Password1" placeholder="Password" name="password" required>
            </div>
            <div class="form-group form-check">
                <input type="checkbox" class="form-check-input" id="Check1" onclick="showPassword()">
                <label class="form-check-label" for="exampleCheck1">Show password</label>
            </div>
            <button type="submit" class="btn btn-primary" value="Login" name="login">Login</button>
            <br>
            <label>Don't have account yet?</label>
            <a href="register.php">Register here</a>
            
        </form>
    </div>

    <script>
        function showPassword() {
            var x = document.getElementById("Password1");
            if (x.type === "password") {
                x.type = "text";
            } else {
                x.type = "password";
            }
        }
    </script>
</body>