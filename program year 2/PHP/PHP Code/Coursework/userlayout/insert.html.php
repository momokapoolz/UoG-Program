<form action="" method="post" enctype="multipart/form-data">
    <div class="form-group">
        <label for="exampleInputquestion">Describe your problem</label>
        <input type="text" name="question_text" class="form-control" placeholder="Enter your question">

        <small id="questionlHelp" class="form-text text-muted">Make sure your question is clear and unduplicate.</small>
        <br>
        <select name="userid" id="">
            <?php
            foreach ($user as $u) {
            ?>
                <option value="<?= $u['id'] ?>"> <?= $u['username'] ?></option>
            <?php
            }
            ?>
        </select>
        <input type="file" name="fileToUpload">

    </div>
    <br>
    <button type="submit" name="submit" value="Add" class="btn btn-primary btn-lg">Post your question</button>
    <br>
</form>