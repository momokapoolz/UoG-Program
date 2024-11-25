<form action="edit.php" method="post">
    <label for='question_text'>Edit question</label>
    <input type="text" name="question_text" value="<?= $question['question_text'] ?>" />
    <br><br>
    <input type="hidden" name="id" value="<?= $question['id'] ?>">
    <button type="submit" name="submit" value="Edit" class="btn btn-primary btn-lg">Edit</button>
</form>