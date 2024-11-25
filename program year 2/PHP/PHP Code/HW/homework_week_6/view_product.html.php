<?php
                foreach ($product as $p) {
        ?>
        <tr>
                <td><?= htmlspecialchars($p['id'], ENT_QUOTES) ?></td>
                <td><?= htmlspecialchars($p['product_name'], ENT_QUOTES) ?></td>
                <td><?= htmlspecialchars($p['product_quantity'], ENT_QUOTES) ?></td>
                <td><?= htmlspecialchars($p['product_price'], ENT_QUOTES) ?></td>
                <td><?= htmlspecialchars($p['product_brand'], ENT_QUOTES) ?></td>
                <td><?= htmlspecialchars($p['product_image'], ENT_QUOTES) ?></td>
                <td><?= htmlspecialchars($p['product_category'], ENT_QUOTES) ?></td>
                <td>
                        <form action="delete.php" method="post">
                                <input type="hidden" name="id" value="<?= $p['id'] ?>">
                                <input type="submit" value="Delete">
                        </form>
                </td>
        </tr>
        <?php } ?>