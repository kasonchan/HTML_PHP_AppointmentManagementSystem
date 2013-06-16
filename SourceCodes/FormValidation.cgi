#!/usr/local/bin/php
<html><head></head><body>
<?php // Sample Form's Processing Script

if (count($_POST) > 0) { // process the submitted form
  // do some simple field checking first...
  
  // make certain something is entered in the Name field
  if (trim($Name=$_POST['Name']) == '') {
    $error = true;
    echo "<div style=\"color:red;\">No name was entered.</div>\n";
    }
    
  // Make certain the zipcode is numeric and in proper
  //   numeric range
  $Zip = $_POST['Zipcode']; // simplification
  if (!(is_numeric($Zip) AND ($Zip >= 500 AND $Zip < 100000))) {
    $error = true;
    echo "<div style=\"color:red;\">Invalid zipcode.</div>\n";
    }
  
  if (!$error) // Display the correct data
    echo "<p>The data you submitted was:</p>\n" .
         "<p>Name: $Name &nbsp; Zipcode: $Zip</p>\n";
  }

// If there was an error, or the form wasn't submitted,
//   display the form
if ($error OR count($_POST) == 0)
  echo <<< EOT
<form method="post" action="">
 &nbsp; &nbsp;Name: <input name="Name" value="$Name" /><br />
Zipcode: <input name="Zipcode" value="$Zip" /><br />
<input type="submit" name="Send" value="Send Info" />
</form>
EOT;
  
?>
</body></html>