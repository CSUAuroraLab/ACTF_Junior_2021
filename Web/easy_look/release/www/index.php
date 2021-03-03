<?php
include "flag";
if(!$_GET['source']){	
	highlight_file(__FILE__);
}
$a = $_GET['a'];
$b = $_GET['b'];
$c = $_GET['c'];
$check = $a and $b;
if($check){
	if($a and $b){
		die("No flag!Try it again!");
	}
	else{
		if($c == md5($c)){
			die($flag);
		}
	}
}
else{
	die("Are You kidding?");
}
