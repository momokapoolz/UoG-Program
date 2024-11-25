<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <link rel="stylesheet" href="style.css">
    <title><?= $title ?></title>
</head>

<body>
    <div class="p-3 mb-2 bg-success text-white" >
        <h1 class="text-center" class="display-1" class="p-3 mb-2 bg-info text-white">Stuck Overflow Admin Site</h1>
    </div>
    <nav class="navbar navbar-light" style="background-color: #e3f2fd;">
        <nav class="navbar navbar-expand-lg bg-body-tertiary" style="background-color: #e3f2fd;">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">Stuck Overflow</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="home.php">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="list.php">Question list</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="insert.php">Post new question</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href='../logout.php'>Logout</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </nav>
    <main>
        <?= $output ?>
    </main>
    <br>
    <a href="../email/index.php">Contact us</a>
    <br>
    <footer>&copy; LGBT 2023</footer>
</body>

</html>