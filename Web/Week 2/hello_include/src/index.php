<?php
echo "提示：源代码有着不能泄露的重要信息<br>";
$allowed = ['hello.php', 'phpinfo.php'];
if (isset($_POST['f1Ie'])) {
    if (strpos($_POST['f1Ie'], 'php://') !== false) {
        die('不允许php://');
    }
    include $_POST['f1Ie'];
} else {
    include 'hello.php';
}
