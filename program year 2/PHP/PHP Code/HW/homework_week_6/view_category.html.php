<?php
                foreach ($category as $c) {
        ?>
        <tr>
                <td><?= htmlspecialchars($c['id'], ENT_QUOTES) ?></td>
                <td><?= htmlspecialchars($c['category'], ENT_QUOTES) ?></td>
                <td>
                        <form action="delete.php" method="post">
                                <input type="hidden" name="id" value="<?= $c['id'] ?>">
                                <input type="submit" value="Delete">
                        </form>
                </td>
        </tr>
        <?php } ?>