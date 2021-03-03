<?php
	error_reporting(0);

	if(isset($_FILES["file"]))
	{
		if(($_FILES["file"]["type"]=="image/jpeg"
		 || $_FILES["file"]["type"]=="image/jpg"
		 || $_FILES["file"]["type"]=="image/gif"
		 || $_FILES["file"]["type"]=="image/png") && $_FILES["file"]["size"] < 1000000)
		 {
		 	move_uploaded_file($_FILES["file"]["tmp_name"], "upload/".$_FILES["file"]["name"]);
			echo "upload success!";
            echo "<br/>";
            echo "The file is in upload/".$_FILES["file"]["name"];
		 }else{
			echo "upload error!";
            echo "<br/>";
		 	echo "Please check the file type and size";
		 }
	}else{
	    highlight_file(__FILE__);
	}

?>
