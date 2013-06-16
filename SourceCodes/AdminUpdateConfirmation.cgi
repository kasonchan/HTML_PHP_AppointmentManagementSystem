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

$updateDate = $_POST['outputDateShort'];
$updateTime = $_POST['outputTimeShort'];

$month = substr($updateDate, 4, 2);
$day = substr($updateDate, 6, 2);
$year = substr($updateDate, 0, 4);
$timeSlot = substr($updateTime, 0, 2) . '-' . substr($updateTime, 2, 2);

$showSubmitbutton = false;
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
	echo "Update Appointment for ";
	echo '<b>' . date(" l, F j, Y", mktime(0, 0, 0, $month, $day, $year)) . ' ' . $timeSlot . '</b>' . ' Confirmation' . '.' . '<br>';
    ?>
  </p>
<!----------------------------------------------------------------------------
   End of display subtitle
  ---------------------------------------------------------------------------->
<?php
if (count($_POST) > 0) 
{ // process the submitted form
  // do some simple field checking first...
  
  // make certain something is entered in the Name field
  if (trim($Name=$_POST['inputName']) == '') 
  {
    $error = true;
    echo "<div style=\"color:red;\">No name was entered.</div>\n";
  }

  // make certain something is entered in the Address field
  if (trim($Address=$_POST['inputAddress']) == '') 
  {
    $error = true;
    echo "<div style=\"color:red;\">No address was entered.</div>\n";
  }
  
  // make certain something is entered in the CityState field
  if (trim($CityState=$_POST['inputCityState']) == '') 
  {
    $error = true;
    echo "<div style=\"color:red;\">No city/state was entered.</div>\n";
  }
  
  // Make certain the zipcode is numeric and in proper
  //   numeric range
  $ZipCode = $_POST['inputZipCode']; // simplification
  if (!(is_numeric($ZipCode) AND ($ZipCode >= 500 AND $ZipCode < 100000))) 
  {
    $error = true;
    echo "<div style=\"color:red;\">Invalid zipcode.</div>\n";
  }
  
  // Make certain the phone is numeric and in proper
  //   numeric range
  $Phone = $_POST['inputPhone']; // simplification
  if (!(is_numeric($Phone) AND ($Phone >= 500 AND $Phone < 9999999999))) 
  {
    $error = true;
    echo "<div style=\"color:red;\">Invalid phone number.</div>\n";
  }

  // make certain something is entered in the PurposeOfVisit field
  $PurposeOfVisit = $_POST['inputPurposeOfVisit'];
  if (trim($PurpostOfVisit=$_POST['inputPurposeOfVisit']) == '') 
  {
    $error = true;
    echo "<div style=\"color:red;\">No purpose of visit was entered.</div>\n";
  }

  $Email = $_POST['inputEmail'];

  $DateLong = $SelectedDayLong;
  $DateShort = $SelectedDayShort;
  if (!$error)
  {
	$showSubmitbutton = true;
  }
}
// ****************************************************************************
// End of form validation
// ****************************************************************************
// If there was an error, or the form wasn't submitted,
// ****************************************************************************
// Update Appointment Confirmation Form
// ****************************************************************************
if ($error OR count($_POST) == 0)
  echo <<< EOT
<form method="post" action="" >
  <table frame='border'>
    <tr><td>  
      Name: <input type="text" name="inputName" value="$updateName"/><br>
      Address: <input type="text" name="inputAddress" value="$updateAddress" /><br>
      City/State: <input type="text" name="inputCityState" value="$updateCityState" /> ZipCode: <input type="text" name="inputZipCode" value="$updateZipCode" /><br>
      Phone: <input type="text" name="inputPhone" value="$updatePhone" /> Email: <input type="text" name="inputEmail" value="$updateEmail" /><br />
      Purpose of Visit: <input type="text" name="inputPurposeOfVisit" value="$updatePurposeOfVisit" /><br />
      Comments: <br />
      <textarea name="inputComments" rows=5 cols=100>$updateComments</textarea><br />
    </td></tr>
  </table>
<input type=submit name=Submit value="Confirm Update Appointment" />

</form>
EOT;
// ****************************************************************************
// End of update appointment confirmation form
// ****************************************************************************
// ****************************************************************************
// End of PHP code
// ****************************************************************************
?>

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
	foreach ($infos as $date => &$dArray)
	{
    		$dateExisted = 'true';
  		// echo "$date<br />\n";
  		foreach ($dArray as $time => &$tArray)
  		{
    			// echo "$time<br/>\n";
    			foreach ($tArray as $field => &$info)
    			{
				if(($field == "Comments") && ($date == $updateDate) && ($time == $updateTime))
				{
					$tArray[$field] = $updateComments;
				}
    			}
  		}
	}

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

$url = 'http://students.csci.unt.edu/~kc0284/AdminUpdateCalendar.cgi';
    echo '<META HTTP-EQUIV=Refresh CONTENT="5; URL='.$url.'">';  
?>

</fieldset>
</body>

</html>

