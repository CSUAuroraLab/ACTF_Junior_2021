<?php
	highlight_file(__FILE__);
	if(isset($_GET['a']) && isset($_GET['b'])){
		$A = $_GET['a'];
		$B = $_GET['b'];
		$A($B);
	}
