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

// Use to test if the post variables are received correctly
// echo $updateName . ' ' . $updateAddress . ' ' . $updateCityState . ' ' . $updateZipCode . ' ' . $updatePhone . ' ' . $updateEmail . ' ' . $updatePurposeOfVisit . '<br>';
// echo $updateNewPatient . ' ' . $updateComments = $_POST['inputComments'] . '<br>';

$updateDateShort = $_POST['newDateShort'];
$updateDate = $_POST['newDateShort'];
$SelectDayShort = $_POST['newDateShort'];
$oldDate = $_POST['oldDateShort'];
$oldTime = $_POST['oldTimeShort'];

// Use to test if the post variables are received correctly
// echo $SelectedDayShort . '<br>';
// echo $updateDate . ' ' . $oldDate . ' ' . $oldTime . '<br>';

$month = substr($updateDate, 4, 2);
$day = substr($updateDate, 6, 2);
$year = substr($updateDate, 0, 4);

// Use to test if the post variables are received correctly
// echo $month . ' ' . $day . ' ' . $year;
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
	echo '<b>' . date(" l, F j, Y", mktime(0, 0, 0, $month, $day, $year)) . '</b>' . '.' . '<br>';
    ?>
  </p>
<!----------------------------------------------------------------------------
   End of display subtitle
  ---------------------------------------------------------------------------->

<form method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>">
<?php
$SelectTime = $_POST['SelectedTime'];
// ****************************************************************************
// PHP code
// ****************************************************************************
// ****************************************************************************
// Display appointment time
// ****************************************************************************
// ****************************************************************************
// Show 8-9 radio button
// ****************************************************************************
$foundTime = false;
$inputInfos = array();
if(file_exists('datafile.dat'))
{
	$inputInfos = include 'datafile.dat';
	foreach ($infos as $date => $dArray) 
	{
  		if($_POST['newDateShort'] == $date)
  		foreach ($dArray as $time => $tArray) 
		{
    			if($time == "0809")
      			$foundTime = true; 
  		}
	}
}
if ($foundTime == false)
{
	if ($_POST['SelectedTime'] == "0809")
  	{
    		echo '<input type=radio name=SelectedTime value="0809" id=0809 checked />';
    		$Time == "0809";
  	}
  	else
  		echo '<input type=radio name=SelectedTime value="0809" id=0809 />';
}
else if ($foundTime == true)
	echo '<input type=radio name=SelectedTime value="0809" id=0809 disabled/>';
echo "8-9" . "</br>";

// ****************************************************************************
// Show 9-10 radio button
// ****************************************************************************
$foundTime = false;
$inputInfos = array();
if(file_exists('datafile.dat'))
{
	$inputInfos = include 'datafile.dat';
	foreach ($infos as $date => $dArray) 
	{
		if($_POST['newDateShort'] == $date)
  		foreach ($dArray as $time => $tArray) 
		{
    			if($time == "0910")
      			$foundTime = true; 
  		}
	}
}
if ($foundTime == false)
{
	if ($_POST['SelectedTime'] == "0910")
  	{
		echo '<input type=radio name=SelectedTime value="0910" id=0910 checked />';
		$Time == "0910";
  	}
	else
	echo '<input type=radio name=SelectedTime value="0910" id=0910 />';
}
else if ($foundTime == true)
	echo '<input type=radio name=SelectedTime value="0910" id=0910 disabled/>';
echo "9-10" . "</br>";

// ****************************************************************************
// Show 10-11 radio button
// ****************************************************************************
$foundTime = false;
$inputInfos = array();
if(file_exists('datafile.dat'))
{
$inputInfos = include 'datafile.dat';
foreach ($infos as $date => $dArray) {
  if($_POST['newDateShort'] == $date)
  foreach ($dArray as $time => $tArray) {
    if($time == "1011")
      $foundTime = true; 
  }
}
}
if ($foundTime == false)
{
  if ($_POST['SelectedTime'] == "1011")
  {
    echo '<input type=radio name=SelectedTime value="1011" id=1011 checked />';
    $Time == "1011";
  }
  else
  echo '<input type=radio name=SelectedTime value="1011" id=1011 />';
}
else if ($foundTime == true)
  echo '<input type=radio name=SelectedTime value="1011" id=1011 disabled/>';
echo "10-11" . "</br>";

// ****************************************************************************
// Show 11-12 radio button
// ****************************************************************************
$foundTime = false;
$inputInfos = array();
if(file_exists('datafile.dat'))
{
$inputInfos = include 'datafile.dat';
foreach ($infos as $date => $dArray) {
  if($_POST['newDateShort'] == $date)
  foreach ($dArray as $time => $tArray) {
    if($time == "1112")
      $foundTime = true; 
  }
}
}
if ($foundTime == false)
{
  if ($_POST['SelectedTime'] == "1112")
  {
    echo '<input type=radio name=SelectedTime value="1112" id=1112 checked />';
    $Time == "1112";
  }
  else
  echo '<input type=radio name=SelectedTime value="1112" id=1112 />';
}
else if ($foundTime == true)
  echo '<input type=radio name=SelectedTime value="1112" id=1112 disabled/>';
echo "11-12" . "</br>";

// ****************************************************************************
// Show 12-13 radio button
// ****************************************************************************
$foundTime = false;
$inputInfos = array();
if(file_exists('datafile.dat'))
{
$inputInfos = include 'datafile.dat';
foreach ($infos as $date => $dArray) {
  if($_POST['newDateShort'] == $date)
  foreach ($dArray as $time => $tArray) {
    if($time == "1213")
      $foundTime = true; 
  }
}
}
if ($foundTime == false)
{
  if ($_POST['SelectedTime'] == "1213")
  {  
    echo '<input type=radio name=SelectedTime value="1213" id=1213 checked />';
    $Time == "1213";
  }
  else
  echo '<input type=radio name=SelectedTime value="1213" id=1213 />';
}
else if ($foundTime == true)
  echo '<input type=radio name=SelectedTime value="1213" id=1213 disabled/>';
echo "12-1" . "</br>";

// ****************************************************************************
// Show 13-14 radio button
// ****************************************************************************
$foundTime = false;
$inputInfos = array();
if(file_exists('datafile.dat'))
{
$inputInfos = include 'datafile.dat';
foreach ($infos as $date => $dArray) {
  if($SelectedDayShort == $date)
  foreach ($dArray as $time => $tArray) {
    if($time == "1314")
      $foundTime = true; 
  }
}
}
if ($foundTime == false)
{
  if ($_POST['SelectedTime'] == "1314")
  {
    echo '<input type=radio name=SelectedTime value="1314" id=1314 checked />';
    $Time == "1314";
  }
  else
  echo '<input type=radio name=SelectedTime value="1314" id=1314 />';
}
else if ($foundTime == true)
  echo '<input type=radio name=SelectedTime value="1314" id=1314 disabled/>';
echo "1-2" . "</br>";

// ****************************************************************************
// Show 14-15 radio button
// ****************************************************************************
$foundTime = false;
$inputInfos = array();
if(file_exists('datafile.dat'))
{
$inputInfos = include 'datafile.dat';
foreach ($infos as $date => $dArray) {
  if($_POST['newDateShort'] == $date)
  foreach ($dArray as $time => $tArray) {
    if($time == "1415")
      $foundTime = true; 
  }
}
}
if ($foundTime == false)
{
  if ($_POST['SelectedTime'] == "1415")
  {
    echo '<input type=radio name=SelectedTime value="1415" id=1415 checked />';
    $Time == "1415";
  }else
  echo '<input type=radio name=SelectedTime value="1415" id=1415 />';
}
else if ($foundTime == true)
  echo '<input type=radio name=SelectedTime value="1415" id=1415 disabled/>';
echo "2-3" . "</br>";

// ****************************************************************************
// Show 15-16 radio button
// ****************************************************************************
$foundTime = false;
$inputInfos = array();
if(file_exists('datafile.dat'))
{
$inputInfos = include 'datafile.dat';
foreach ($infos as $date => $dArray) {
  if($_POST['newDateShort'] == $date)
  foreach ($dArray as $time => $tArray) {
    if($time == "1516")
      $foundTime = true; 
  }
}
}
if ($foundTime == false)
{
  if ($_POST['SelectedTime'] == "1516")
  {
    echo '<input type=radio name=SelectedTime value="1516" id=1516 checked />';
    $Time == "1516";
  }
  else
  echo '<input type=radio name=SelectedTime value="1516" id=1516 />';
}
else if ($foundTime == true)
  echo '<input type=radio name=SelectedTime value="1516" id=1516 disabled/>';
echo "3-4" . "</br>";

// ****************************************************************************
// Show 16-17 radio button
// ****************************************************************************
$foundTime = false;
$inputInfos = array();
if(file_exists('datafile.dat'))
{
$inputInfos = include 'datafile.dat';
foreach ($infos as $date => $dArray) {
  if($_POST['newDateShort'] == $date)
  foreach ($dArray as $time => $tArray) {
    if($time == "1617")
      $foundTime = true; 
  }
}
}
if ($foundTime == false)
{
  if ($_POST['SelectedTime'] == "1617")
  {
    echo '<input type=radio name=SelectedTime value="1617" id=1617 checked />';
    $Time == "1617";
  }
  else
  echo '<input type=radio name=SelectedTime value="1617" id=1617 />';
}
else if ($foundTime == true)
  echo '<input type=radio name=SelectedTime value="1617" id=1617 disabled/>';
echo "4-5" . "</br>";

// ****************************************************************************
// End of display appointment time
// ****************************************************************************

// ****************************************************************************
// Form Validation
// ****************************************************************************
// Sample Form's Processing Script
if (count($_POST) > 0) 
{ 
	// Process the submitted form
  	// Do some simple field checking first...

  	// If not yet chose time  
	if($_POST['SelectedTime'] == '')
	{  
		$error = true;
		echo "<div style=\"color:red;\">No time was selected.</div>\n";
	}

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
// Form input
// ****************************************************************************
if ($error OR count($_POST) == 0)
  echo <<< EOT
<input type="hidden" name="inputName" value="$updateName" />
<input type="hidden" name="inputAddress" value="$updateAddress" />
<input type="hidden" name="inputCityState" value="$updateCityState" />
<input type="hidden" name="inputZipCode" value="$updateZipCode" />
<input type="hidden" name="inputPhone" value="$updatePhone" />
<input type="hidden" name="inputEmail" value="$updateEmail" />
<input type="hidden" name="inputPurposeOfVisit" value="$updatePurposeOfVisit" />
<textarea name="inputComments" rows=0 cols=0 style="visibility:hidden;">"$updateComments"</textarea>
<input type="hidden" name="oldDateShort" value="$oldDate" />
<input type="hidden" name="oldTimeShort" value="$oldTime" />
<input type="hidden" name="updateTimeShort" value="$SelectTime" >
<input type="hidden" name="newDateShort" value="$SelectDayShort" />
<input type="hidden" name="inputDay" id="SelectedDay" size="30" /><br />
<p><input type="submit" value="Select new Appointment Time"/><br /></p>
EOT;
// ****************************************************************************
// End of form input
// ****************************************************************************
// ****************************************************************************
// End of PHP code
// ****************************************************************************
?>
</form>

<form method="post" action="AdminSelectConfirm.cgi">
<?php
	if($showSubmitbutton == false)
		echo "<input type=\"submit\" name=\"Submit\" value=\"Confirm Submit new Appointment Date\"  style=\"display:none;\" />";
	else if($showSubmitbutton == true)
		echo "<input type=\"submit\" name=\"Submit\" value=\"Confirm Submit new Appointment Date\" />";
?>
<input type="hidden" name="inputName" value="<?=$_POST['inputName']; ?>"/>
<input type="hidden" name="inputAddress" value="<?=$_POST['inputAddress']; ?>" />
<input type="hidden" name="inputCityState" value="<?=$_POST['inputCityState']; ?>" />
<input type="hidden" name="inputZipCode" value="<?=$_POST['inputZipCode']; ?>" />
<input type="hidden" name="inputPhone" value="<?=$_POST['inputPhone']; ?>" />
<input type="hidden" name="inputEmail" value="<?=$_POST['inputEmail']; ?>" />
<input type="hidden" name="inputPurposeOfVisit" value="<?=$_POST['inputPurposeOfVisit']; ?>" />
<textarea name="inputComments" rows=0 cols=0  style="visibility:hidden;"><?=$_POST['inputComments']; ?></textarea>
<input type="hidden" name="oldDateShort" value="<?=$_POST['oldDateShort']; ?>" />
<input type="hidden" name="oldTimeShort" value="<?=$oldTime; ?>" />
<input type="hidden" name="updateTimeShort" value="<?=$_POST['SelectedTime']; ?>" >
<input type="hidden" name="newDateShort" value="<?=$_POST['newDateShort']; ?>" />
<input type="hidden" name="inputDay" id="SelectedDay" size="30" /><br />
</form>


</fieldset>
</body>

</html>

