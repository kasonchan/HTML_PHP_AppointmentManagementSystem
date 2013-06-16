#!/usr/local/bin/php

<!--
// *************************************************************
// Project
// CSCE 4410, Summer 2012
// Student: Ka Son Chan KaSonChan@my.unt.edu
// Instructor: Don Retzlaff
// Date: August 8, 2012
//
// AdminDeleteConfirmation.cgi
// Description: AdminDeleteConfirmation.cgi displays the
// confirmation for the selected client's info is deleted.
// *************************************************************
-->

<html>
<head>
</head>

<body>
<?php
$updateName = $_POST['inputName'];
$updateAddress = $_POST['inputAddress'];
$updateCityState = $_POST['inputCityState'];
$updateZipCode = $_POST['inputZipCode'];
$updatePhone = $_POST['inputPhone'];
$updateEmail = $_POST['inputEmail'];
$updatePurposeOfVisit = $_POST['inputPurposeOfVisit'];
$updateNewPatient = $_POST['inputNewPatient'];
$updateComments = $_POST['inputComments'];

$updateDate = $_POST['outputDateShort'];
$updateTime = $_POST['outputTimeShort'];

$month = substr($updateDate, 4, 2);
$day = substr($updateDate, 6, 2);
$year = substr($updateDate, 0, 4);
$timeSlot = substr($updateTime, 0, 2) . '-' . substr($updateTime, 2, 2);
?>

<fieldset>
<!----------------------------------------------------------------------------
   Display title
  ---------------------------------------------------------------------------->
<legend>
	<p style="font-size:20pt; font-weight:bold;" align=center>
    		Dr. Fred's Admin Appointment Calendar
  	</p>
</legend>
<!----------------------------------------------------------------------------
   End of display title
  ---------------------------------------------------------------------------->

<!----------------------------------------------------------------------------
   Display subtitle
  ---------------------------------------------------------------------------->
<p style="font-size:16pt;">
	<?php
		echo "Delete Appointment for ";
		echo '<b>' . date(" l, F j, Y", mktime(0, 0, 0, $month, $day, $year)) . ' ' . $timeSlot . '</b>' . ' Confirmation' . '.' . '<br>';
    	?>
 </p>
<!----------------------------------------------------------------------------
   End of display subtitle
  ---------------------------------------------------------------------------->

<?php
// ****************************************************************************
// Reading the whole data file to inputInfo array
// Also Use to test if reading the whole data file correctly
// ****************************************************************************
$dateExisted = 'false';
$inputInfos = array();
if(file_exists('datafile.dat'))
{
	$inputInfos = include 'datafile.dat';

	foreach ($infos as $date => $dArray)
	{
    		$dateExisted = 'true';
  		// echo "$date<br />\n";
  		foreach ($dArray as $time => $tArray)
  		{
    			// echo "$time<br/>\n";
    			foreach ($tArray as $field => $info)
    			{
      				// echo "$field => $info<br />\n";
				
    			}
  		}
	}
}
// ****************************************************************************
// End of reading the whole data file to inputInfo array
// ****************************************************************************
// ****************************************************************************
// Delete the selected client info array
// ****************************************************************************
foreach ($infos as $date => &$dArray)
{
  	foreach ($dArray as $time => $tArray)
  	{
    		if($time == $updateTime && ($date == $updateDate))
		{
			unset($dArray[$time]);
		}
			
  	}
}
// ****************************************************************************
// End of delete the selected client info array
// ****************************************************************************
// ****************************************************************************
// Add the new client info and write to the datafile
// ****************************************************************************
// Convert the data into a PHP compatible data stream
$data = "<?php\n\$infos = " . var_export($infos,true) . ";\n?" . ">\n";

// Write the data to a file
$fh = fopen('datafile.dat','w');
fputs ($fh,$data);
fclose ($fh);
// ****************************************************************************
// End of add the new client info and write to the datafile
// ****************************************************************************
// ****************************************************************************
// Redirect to AdminUpdateCalendar.cgi
// ****************************************************************************
$url = 'http://students.csci.unt.edu/~kc0284/AdminUpdateCalendar.cgi';
    echo '<META HTTP-EQUIV=Refresh CONTENT="5; URL='.$url.'">';  


// ****************************************************************************
// End of redirect to AdminUpdateCalendar.cgi
// ****************************************************************************
?>
</fieldset>
</body>

</html>

