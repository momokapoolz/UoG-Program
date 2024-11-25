<form action="" method="post">
    <label for='joketext'>Type your joke here;</label>
    <textarea name="joketext" rows="3" cols="40"></textarea>
    Author:
    <select name="jokeauthor" id="">
        <?php
        foreach($authors as $a)
        ?>
        <option value="<?= $a['id'] ?>">
            <?=$a['name'] ?>
        </option>
    </select>
    <input type="submit" name="submit" value="Add">
</form>

