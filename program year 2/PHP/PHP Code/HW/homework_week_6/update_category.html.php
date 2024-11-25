<form action="" method="post">
    Edit category:
    <br><br>
    <input type="text" name="category">
    <br><br>
    <input type="hidden" name="id" value="<?= $category['id']?>">
    <input type="submit" name="submit" value="Edit">
</form>