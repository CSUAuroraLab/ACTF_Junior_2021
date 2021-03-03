<?php
	highlight_file(__FILE__);
	if(isset($_GET['url'])){
		$url = $_GET['url'];
		$ch = curl_init();
		curl_setopt($ch, CURLOPT_URL, $url);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
		curl_setopt($ch, CURLOPT_HEADER, 0);
		$output = curl_exec($ch);
		echo $output;
    }
	// flag is in 192.168.54.3 :-)
    // view http://192.168.54.3/
