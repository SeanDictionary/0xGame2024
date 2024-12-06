<?php
highlight_file(__FILE__);
$cmd = $_REQUEST['cmd'] ?? 'ls';
if (strpos($cmd, ' ') !== false) {
    echo strpos($cmd, ' ');
    die('no space allowed');
}
@exec($cmd); // 没有回显怎么办？