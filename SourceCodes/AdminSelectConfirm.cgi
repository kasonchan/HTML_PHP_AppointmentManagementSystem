#!/usr/local/bin/php

<!--
// *************************************************************
// Project
// CSCE 4410, Summer 2012
// Student: Ka Son Chan KaSonChan@my.unt.edu
// Instructor: Don Retzlaff
// Date: August 8, 2012
//
// AdminUpdateConfirmation.cgi
// Description: AdminUpdateAppoint.cgi let the admins to update
// client's infos and provide comments.
// It shows all the infos of the selected client from
// AdminWeekAppointmentSchedule.cgi.
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

// Use to test if the post variables are receive correctly
// echo $updateName . ' ' . $updateAddress . ' ' . $updateCityState . ' ' . $updateZipCode . ' ' . $updatePhone . ' ' . $updateEmail . ' ' . $updatePurposeOfVisit . '<br>';
// echo $updateNewPatient . ' ' . $updateComments = $_POST['inputComments'] . '<br>';

$updateDate = $_POST['newDateShort'];
$updateTime = $_POST['updateTimeShort'];
$oldDate = $_POST['oldDateShort'];
$oldTime = $_POST['oldTimeShort'];

// Use to test if the post variables are receive correctly
// echo $SelectedDayShort . '<br>';
// echo $updateDate . ' ' . $updateTime . ' ' . $oldDate . ' ' . $oldTime . '<br>';

$month = substr($updateDate, 4, 2);
$day = substr($updateDate, 6, 2);
$year = substr($updateDate, 0, 4);
?>

<fieldset>
<!----------------------------------------------------------------------------
   Display title
  ---------------------------------------------------------------------------->
  <legend><p style="font-size:20pt; font-weight:bold;" align=center>
    Dr. Fred's Admin Appointment Calendar
  </p></legend>
<!----------------------------------------------------------------------------
   End of display title
  ---------------------------------------------------------------------------->

<!----------------------------------------------------------------------------
   Display subtitle
  ---------------------------------------------------------------------------->
  <p style="font-size:16pt;">
    <?php
	echo "Update Appointment to ";
	echo '<b>' . date(" l, F j, Y", mktime(0, 0, 0, $month, $day, $year)) . '</b>' . ' Confirmation.' . '<br>';
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
$dateExisted == 'false';
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
	foreach ($infos as $date => &$dArray)
	{
  		// echo "$date<br />\n";
  		foreach ($dArray as $time => &$tArray)
  		{
    			if($time == $_POST['oldTimeShort'] && ($date == $_POST['oldDateShort']))
			{
				unset($dArray[$time]);
			}
			
  		}
	}
	

// ****************************************************************************
// Add the new client info and write to the datafile
// ****************************************************************************
$PersonalInfoArray = array ('Name' => $_POST['inputName'], 'Address' => $_POST['inputAddress'], 'City/State' => $_POST['inputCityState'], 'ZipCode' => $_POST['inputZipCode'], 'Phone' => $_POST['inputPhone'], 'Email' => $_POST['inputEmail'], 'PurposeOfVisit' => $_POST['inputPurposeOfVisit'], 'NewPatient' => $_POST['inputNewPatient'], 'Comments' => $_POST['inputComments']);
if($dateExisted == 'false')
{
  $TimeArray = array ($_POST['updateTimeShort'] => $PersonalInfoArray);
  $infos[$_POST['newDateShort']] = $TimeArray;
}
else
{
  $TimeArray = array ($updateTime => $PersonalInfoArray);
  $infos[$_POST['newDateShort']][$_POST['updateTimeShort']] = $PersonalInfoArray;
}

// Convert the data into a PHP compatible data stream
$data = "<?php\n\$infos = " . var_export($infos,true) . ";\n?" . ">\n";

// Write the data to a file
$fh = fopen('datafile.dat','w');
fputs ($fh,$data);
fclose ($fh);
// ****************************************************************************
// End of add the new client info and write to the datafile
// ****************************************************************************

$url = 'http://students.csci.unt.edu/~kc0284/AdminUpdateCalendar.cgi';
    echo '<META HTTP-EQUIV=Refresh CONTENT="5; URL='.$url.'">';  
?>


</fieldset>
</body>

</html>

