<?php
echo "<h1>你知道http协议吗？</h1>";
echo "<h2>你知道怎么修改请求包吗？</h2>";
echo "<!-- 或许你需要使用工具 -->";
$flag = '0xgame{1cd6a904-725f-11ef-aafb-d4d8533ec05c}'; #均分成9段
$flags = str_split($flag, 5);
if ($_SERVER['HTTP_USER_AGENT'] != 'x1cBrowser') {
    die('请使用x1cBrowser浏览器访问');
}
echo $flags[0];
if (!isset($_GET['hello'])) {
    die('<br>请用GET方式传递hello=world');
}
echo $flags[1];
if ($_GET['hello'] != 'world') {
    die('<br>hello参数值不正确');
}
echo $flags[2];
if (!isset($_POST['web'])) {
    die('<br>请用POST方式传递web=security');
}
echo $flags[3];
if ($_POST['web'] != 'security') {
    die('<br>web参数值不正确');
}
echo $flags[4];
if (!isset($_COOKIE['flag'])) {
    die('<br>请设置cookie flag=secret');
}
echo $flags[5];
if ($_COOKIE['flag'] != 'secret') {
    die('<br>cookie flag值不正确');
}
echo $flags[6];
if ($_SERVER['HTTP_REFERER'] != 'http://localhost:8080/') {
    die('<br>请从http://localhost:8080/访问');
}
echo $flags[7];
if ($_SERVER['HTTP_X_FORWARDED_FOR'] != '127.0.0.1') {
    die('<br>请从127.0.0.1访问');
}
echo $flags[8]."<br>";
echo '<h1>看来你知道http协议了</h1>';