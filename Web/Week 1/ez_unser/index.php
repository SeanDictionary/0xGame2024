<?php
highlight_file(__FILE__);
class Man{
    private $name="原神，启动";
    public function __wakeup()
    {
        echo str_split($this->name);
    }
}
class What{
    private $Kun="两年半";
    public function __toString()
    {

        echo $this->Kun->hobby;
        return "Ok";
    }
}
class Can{
    private $Hobby="唱跳rap篮球";
    public function __get($name)
    {
        var_dump($this->Hobby);
    }
}
class I{
    private $name="Kobe";
    public function __debugInfo()
    {
        $this->name->say();
    }

}
class Say{
    private $evil;
    public function __call($name, $arguments)
    {
        $this->evil->Evil();
    }
}
class Mamba{
    public function Evil()
    {
        $filename=time().".log";
        file_put_contents($filename,$_POST["content"]);
        echo $filename;

    }
}
class Out{
    public function __call($name,$arguments)
    {
        $o = "./".str_replace("..", "第五人格",$_POST["o"]);
        $n = $_POST["n"];
        rename($o,$n);
    }
}
unserialize($_POST["data"]);