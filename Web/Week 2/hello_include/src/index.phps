<?php
echo "Hint: The source code contains important information that must not be disclosed.<br>";
$allowed = ['hello.php', 'phpinfo.php'];
if (isset($_POST['f1Ie'])) {
    if (strpos($_POST['f1Ie'], 'php://') !== false) {
        die('不允许php://');
    }
    include $_POST['f1Ie'];
} else {
    include 'hello.php';
}
