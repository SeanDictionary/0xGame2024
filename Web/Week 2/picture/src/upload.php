<?php
error_reporting(E_ALL);
if (!isset($_FILES["file"])) {
    exit();
}
$file = $_FILES["file"];
if ($file["size"] > 20480) {
    echo "文件过大！";
    exit();
}
$ima = getimagesize($file["tmp_name"]);
if (($file["type"] == "image/jpeg") || ($file["type"] == "image/jpg")) {
    if (strpos($file["name"], "php")) {
        echo "为什么你的文件名里面有php呢？";
    } elseif (!$ima || ($ima["mime"] != "image/jpeg" && $ima["mime"] != "image/jpg")) {
        echo "不是，你以为你说你是jpg图片就是jpg图片了？";
    } else {
        $fileName = 'uploads/' . uniqid() . '-' . $file['name'];
        move_uploaded_file($file['tmp_name'], $fileName);
        echo "成功上传！文件位于：$fileName";
    }
} else {
    echo "仅限上传jpg文件";
}
