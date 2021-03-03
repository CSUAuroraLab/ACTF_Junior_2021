<?php
highlight_file(__FILE__);
include "flag.php";
class User{
	private $Username = "0xDktb";
	private $Password = "0xDktb111";

	function __construct(){
		$Username = "0xDktb";
		$Password = "0xDktb123";
	}


	function isAdmin(){
		if($this->Username == "admin"){
			return true;
		}
		return false;
	}

	function __destruct(){
		echo "Hello ".$this->Username;
	}
}

$user = new User();

if($_GET['user']){
	$user = unserialize($_GET['user']);
}

if($user->isAdmin()){
	echo $flag;
}
?>