#!/usr/local/bin/php

<!--
// *************************************************************
// Project
// CSCE 4410, Summer 2012
// Student: Ka Son Chan KaSonChan@my.unt.edu
// Instructor: Don Retzlaff
// Date: August 8, 2012
//
// AdminUpdateAppointment.cgi
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
$SelectedDate = $_POST['inputDateShort'];
$SelectedDateLong = $_POST['inputDateLong'];
$SelectedTime = $_POST['SelectedDateTime'];
$month = substr($SelectedDate, 4, 2);
$day = substr($SelectedDate, 6, 2);
$year = substr($SelectedDate, 0, 4);
$addDay = substr($SelectedTime, 0, 1);
$findDate = $SelectedDate + $addDay;
$findTime = substr($SelectedTime, 1, 4);
$timeSlot = substr($SelectedTime, 1, 2) . '-' . substr($SelectedTime, 3, 2);
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
	echo '<b>' . $SelectedDateLong . date(" F j, Y", mktime(0, 0, 0, $month, $day + $addDay, $year)) . ' ' . $timeSlot . '</b>' . '.' . '<br>';
    ?>
  </p>
<!----------------------------------------------------------------------------
   End of display subtitle
  ---------------------------------------------------------------------------->

<?php
// Use to test if the data was passing correctly
// echo 'addDay = ' . $addDay . '; ' . 'findDate = ' . $findDate . '; ' . 'findTime = ' . $findTime . '<br>';

if (count($_POST) > 0) 
{ 
	// Process the submitted form
  	// Do some simple field checking first...

	if($_POST['inputDateShort'] == '' || $_POST['SelectedDateTime'] == '')
	{
		$error = true;
		echo "<div style=\"color:red;\">No client was selected.</div>\n";
	}
}
echo "<form method=\"post\" action=\"AdminUpdateCalendar.cgi\">";
	echo "<p>" . "<input type=\"submit\" name=\"UpdateAppointment\" value=\"Select another client\" />" . "</p>";
echo "</form>";

$inputInfos = array();
if(file_exists('datafile.dat'))
{
	$inputInfos = include 'datafile.dat';
	foreach ($infos as $date => $dArray) 
	{
		if("$findDate" == $date)
  		foreach ($dArray as $time => $tArray) 
		{
    			if("$findTime" == $time)
      			foreach ($tArray as $field => $info)
   			{
				if($field == "Name")
					$updateName = $info;
				else if($field == "Address")
					$updateAddress = $info;
				else if($field == "City/State")
					$updateCityState = $info;
				else if($field == "ZipCode")
					$updateZipCode = $info;
				else if($field == "Phone")
					$updatePhone = $info;
				else if($field == "Email")
					$updateEmail = $info;
				else if($field == "PurposeOfVisit")
					$updatePurposeOfVisit = $info;
				else if($field == "NewPatient")
					$updateNewPatient = $info;
				else if($field == "Comments")
					$updateComment = $info;

			}
		}
	}
}

?>
<!----------------------------------------------------------------------------
   Update Appointment Form
   It links to AdminUpdateConfirmation.cgi
  ---------------------------------------------------------------------------->
<form method="post" action="AdminUpdateConfirmation.cgi">
  <table frame='border'>
    <tr><td>  
      Name: <input type="text" name="inputName" value="<?=$updateName; ?>"/><br>
      Address: <input type="text" name="inputAddress" value="<?=$updateAddress; ?>" /><br>
      City/State: <input type="text" name="inputCityState" value="<?=$updateCityState; ?>" /> ZipCode: <input type="text" name="inputZipCode" value="<?=$updateZipCode; ?>" /><br>
      Phone: <input type="text" name="inputPhone" value="<?=$updatePhone; ?>" /> Email: <input type="text" name="inputEmail" value="<?=$updateEmail; ?>" /><br />
      Purpose of Visit: <input type="text" name="inputPurposeOfVisit" value="<?=$updatePurposeOfVisit; ?>" /><br />
      <?php 
	if($updateNewPatient == "Yes")
       	echo "<input type=\"checkbox\" name=\"inputNewPatient\" checked />" . ' New Patient?' . '<br>';
	else
       	echo "<input type=\"checkbox\" name=\"inputNewPatient\" />" . ' New Patient?' . '<br>';
	?>
      Comments: <br />
      <textarea name="inputComments" rows=5 cols=100><?php echo $updateComment; ?></textarea><br />
      <input type="hidden" name="outputDateShort" value="<?=$findDate; ?>"/><br>
      <input type="hidden" name="outputTimeShort" value="<?=$findTime; ?>"/><br>
    </td></tr>
  </table>
<input type="submit" name="UpdateAppointment" value="Update Appointment" />
</form>
<!----------------------------------------------------------------------------
   End of update Appointment Form
  ---------------------------------------------------------------------------->
<!----------------------------------------------------------------------------
   Select another date form 
   It links to AdminSelectAnotherDate.cgi
  ---------------------------------------------------------------------------->
<form method="post" action="AdminSelectAnotherDay.cgi">
<input type="submit" name="SelectAnotherDate" value="Select Another Date" />
      <input type="hidden" name="inputName" value="<?=$updateName; ?>"/>
      <input type="hidden" name="inputAddress" value="<?=$updateAddress; ?>" />
      <input type="hidden" name="inputCityState" value="<?=$updateCityState; ?>" /><input type="hidden" name="inputZipCode" value="<?=$updateZipCode; ?>" />
      <input type="hidden" name="inputPhone" value="<?=$updatePhone; ?>" /><input type="hidden" name="inputEmail" value="<?=$updateEmail; ?>" />
      <input type="hidden" name="inputPurposeOfVisit" value="<?=$updatePurposeOfVisit; ?>" />
      <?php 
	if($updateNewPatient == "Yes")
       	echo "<input type=\"checkbox\" name=\"inputNewPatient\" checked style=\"display:none;\" />";
	else
       	echo "<input type=\"checkbox\" name=\"inputNewPatient\" style=\"display:none;\" />";
	?>
      <textarea name="inputComments" rows=0 cols=0 style="visibility:hidden;" ><?php echo $updateComment; ?></textarea>
      <input type="hidden" name="outputDateShort" value="<?=$findDate; ?>"/>
      <input type="hidden" name="outputTimeShort" value="<?=$findTime; ?>"/>
</form>
<!----------------------------------------------------------------------------
   End of select another date form
  ---------------------------------------------------------------------------->
<!----------------------------------------------------------------------------
   Delete appointment form
   It links to AdminDeleteConfirmation.cgi
  ---------------------------------------------------------------------------->
<form method="post" action="AdminDeleteConfirmation.cgi">
<input type="submit" name="Delete Appointment" value="Delete Appointment" />
      <input type="hidden" name="inputName" value="<?=$updateName; ?>"/>
      <input type="hidden" name="inputAddress" value="<?=$updateAddress; ?>" />
      <input type="hidden" name="inputCityState" value="<?=$updateCityState; ?>" /><input type="hidden" name="inputZipCode" value="<?=$updateZipCode; ?>" />
      <input type="hidden" name="inputPhone" value="<?=$updatePhone; ?>" /><input type="hidden" name="inputEmail" value="<?=$updateEmail; ?>" />
      <input type="hidden" name="inputPurposeOfVisit" value="<?=$updatePurposeOfVisit; ?>" />
      <?php 
	if($updateNewPatient == "Yes")
       	echo "<input type=\"checkbox\" name=\"inputNewPatient\" checked style=\"display:none;\" />";
	else
       	echo "<input type=\"checkbox\" name=\"inputNewPatient\" style=\"display:none;\" />";
	?>
      <textarea name="inputComments" rows=0 cols=0 style="visibility:hidden;" ><?php echo stripslashes($updateComment); ?></textarea>
      <input type="hidden" name="outputDateShort" value="<?=$findDate; ?>"/>
      <input type="hidden" name="outputTimeShort" value="<?=$findTime; ?>"/>
</form>
<!----------------------------------------------------------------------------
   End of delete appointment form
  ---------------------------------------------------------------------------->
<!----------------------------------------------------------------------------
   Logout form
   It links to AdminLogoutConfirmation.cgi
  ---------------------------------------------------------------------------->
<form method="post" action="AdminLogoutConfirmation.cgi">
	<p><input type="submit" name="Logout" value="Logout" /></p>
</form>
<!----------------------------------------------------------------------------
   End of logout from
  ---------------------------------------------------------------------------->
</fieldset>
</body>

</html>

