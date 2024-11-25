<table>
        <tr>
                <th>Employee first name</th>
                <th>Employee last name</th>
                <th>Employee email</th>
        </tr>
        <?php
                foreach ($employee as $e) {
        ?>
        <tr>
                <td><?= htmlspecialchars($e['first_name'], ENT_QUOTES) ?></td>
                <td><?= htmlspecialchars($e['last_name'], ENT_QUOTES) ?></td>
                <td><?= htmlspecialchars($e['email'], ENT_QUOTES) ?></td>
                <td>
                        <form action="delete.php" method="post">
                                <input type="hidden" name="id" value="<?= $e['id'] ?>">
                                <input type="submit" value="Delete">
                        </form>
                </td>
        </tr>
        <?php } ?>
</table>