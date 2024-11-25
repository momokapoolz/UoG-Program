<form action="" method="post">
    Edit joke:
    <br><br>
    <input type="text" name="joketext">
    <br><br>
    <input type="hidden" name="id" value="<?= $joke['id']?>">
    <input type="submit" name="submit" value="Edit">
</form>