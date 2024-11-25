<form action="" method="post">
    <label for='book_title'>Insert new book</label>
    <textarea name="book_title" rows="3" cols="40"></textarea>
    <select name="genre_id" id="">
        <?php
        foreach($genres as $g){
        ?>
        <option value="<?=$g['genre_id']?>"> <?=$g['genre_name']?></option>
        <?php
        } 
        ?>
    </select>
    <input type="submit" name="submit" value="Add">
</form>

