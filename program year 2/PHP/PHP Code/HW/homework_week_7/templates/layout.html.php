<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="jokes.css">
        <title><?=$title?></title>
    </head>
    <body>
        <header><h1>Library</h1></header>
        <nav>
            <ul>
                <li><a href="listbook.php">Books List</a></li>
                <li><a href="addbook.php">Add a new book</a></li>
            </ul>
        </nav>
        <main>
            <?=$output?>
        </main>
        <footer>&copy; IJDB 2023</footer>
    </body>
</html>