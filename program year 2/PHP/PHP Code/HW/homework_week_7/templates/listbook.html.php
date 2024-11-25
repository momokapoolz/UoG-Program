<?php
foreach($books as $b): ?>
        <blockquote>
        <?=htmlspecialchars($b['book_title'], ENT_QUOTES,'UTF-8')?>
        <br>
        <?=htmlspecialchars($b['genre_name'], ENT_QUOTES, 'UTF-8'); ?></a>


        </blockquote>
        <?php endforeach;?>

