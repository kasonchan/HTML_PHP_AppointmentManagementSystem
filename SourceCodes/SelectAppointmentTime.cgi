#!/usr/local/bin/php

<!--
// *************************************************************
// Project
// CSCE 4410, Summer 2012
// Student: Ka Son Chan KaSonChan@my.unt.edu
// Instructor: Don Retzlaff
// Date: August 8, 2012
//
// SelectAppointmentTime.cgi
// Description: SelectAppointmentTime.cgi is the client 
// interface for the client to select appointment time after
// selecting the date from the homepage.cgi.
// It shows the time slots of the selected day and client
// information form.
// *************************************************************
-->

<html>
<head>
  <title>Welcome to Dr. Fred's Appointment Calendar</title>
</head>
<body>

  <?php
    // ************************************************************************
    // Use to test if variables values pass from previous page 
    // ************************************************************************
    $Day = $_POST["inputDay"];
    $SelectedDayLong = $_POST["inputDateLong"];
    $SelectedDayShort = $_POST["inputDateShort"];
    // echo $Day . "<br>" . $SelectedDayLong . "<br>" . $SelectedDayShort;
    $showSubmitbutton = false;
  ?>

<fieldset>
<!--Display title-->
  <legend><p style="font-size:20pt; font-weight:bold;">
    <?php
      echo "Dr. Fred's Appointment Calendar";
    ?>
  </p></legend>
<!--End of dsiaply title-->

<!--Display subtitle-->
  <p style="font-size:16pt;">
  <?php
    echo "Select New Appointment Time<br>";
    echo "for " . '<b>' . $_POST["inputDateLong"] . '</b>' . '.' . "<br>";
  ?>
  </p>
<!--End of display subtitle-->

<input type='hidden' name='inputDateLong' value="<?=$SelectedDayLong; ?>">
<input type='hidden' name='inputDateShort' value="<?=$SelectedDayShort; ?>">


<?php
	if($SelectedDayShort == '')
	{
		$error = true;
		echo "<div style=\"color:red;\">No date was selected.</div>\n";
	}
?>

<!----------------------------------------------------------------------------
// Display select different appointment button
  ---------------------------------------------------------------------------->
<form action="http://students.csci.unt.edu/~kc0284/Homepage.cgi">
  <p><input type="submit" name="inputDate" value="Select Different Appointment Day"/></p>
</form>
<!----------------------------------------------------------------------------
// End of display select different appointment button
  ---------------------------------------------------------------------------->

<form method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>">
<?php
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
foreach ($infos as $date => $dArray) {
  if($SelectedDayShort == $date)
  foreach ($dArray as $time => $tArray) {
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
foreach ($infos as $date => $dArray) {
  if($SelectedDayShort == $date)
  if($SelectedDayShort == $date)
  foreach ($dArray as $time => $tArray) {
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
  if($SelectedDayShort == $date)
  if($SelectedDayShort == $date)
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
  if($SelectedDayShort == $date)
  if($SelectedDayShort == $date)
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
  if($SelectedDayShort == $date)
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
  if($SelectedDayShort == $date)
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
  if($SelectedDayShort == $date)
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
  if($SelectedDayShort == $date)
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
// Show sentence Select an available appointments time above
// ****************************************************************************
echo "<i>Select an available appointments time above</i>" . '<br>' . '<br>';

// ****************************************************************************
// Save SelectedTimeLong
// ****************************************************************************
$SelectedTimeShort = $_POST['SelectedTime'];
if($SelectedTimeShort == "0809")
{
    // echo $SelectedTimeShort;
    $SelectedTimeLong = "8 am - 9 am";
}
if($SelectedTime == "0910")
{
    // echo $SelectedTime;
    $SelectedTimeLong = "9 am - 10 am";
}
if($SelectedTime == "1011")
{
    // echo $SelectedTime;
    $SelectedTimeLong = "10 am - 11 am";
}
if($SelectedTime == "1112")
{
    // echo $SelectedTime;
    $SelectedTimeLong = "11 am - 12 pm";
}
if($SelectedTime == "1213")
{
    // echo $SelectedTime;
    $SelectedTimeLong = "12 pm - 1 pm";
}
if($SelectedTime == "1314")
{
    // echo $SelectedTime;
    $SelectedTimeLong = "1 pm - 2 am";
}
if($SelectedTime == "1415")
{
    // echo $SelectedTime;
    $SelectedTimeLong = "2 pm - 3 pm";
}
if($SelectedTime == "1516")
{
    // echo $SelectedTime;
    $SelectedTimeLong = "3 pm - 4 pm";
}
if($SelectedTime == "1617")
{
    // echo $SelectedTime;
    $SelectedTimeLong = "4 pm - 5 pm";
}
// ****************************************************************************
// End of save SelectedTimeLong
// ****************************************************************************

// ****************************************************************************
// Form Validation
// ****************************************************************************
// Sample Form's Processing Script
if (count($_POST) > 0) 
{ 
	// Process the submitted form
  	// Do some simple field checking first...


	if($SelectedDayShort == '')
	{
		$error = true;
		echo "<div style=\"color:red;\">No date was selected.</div>\n";
	}

  	// If not yet chose time  
	if($SelectedTimeShort == '')
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
  <table frame="border">
    <tr><td>  
      *Name: <input type="text" name="inputName" value="$Name" /><br />
      *Address: <input type="text" name="inputAddress" value="$Address" size="50" /><br />
      *City/State: <input type="text" name="inputCityState" value="$CityState" /> *ZipCode: <input type="text" name="inputZipCode" value="$ZipCode" /><br />
      *Phone: <input type="text" name="inputPhone" value="$Phone" /> Email: <input type="text" name="inputEmail" value="$Email" /><br />
      *Purpose of Visit? <input type="text" name="inputPurposeOfVisit" value="$PurposeOfVisit" size="100" /><br />
      <input type="checkbox" name="inputNewPatient"> New Patient?<br>
      <!----------------------------------------------------------------------
         Use to test if the input
      ---------------------------------------------------------------------->
      <input type="hidden" name='inputDateLong' value="$DateLong">
      <input type="hidden" name='inputDateShort' value="$DateShort">
      <input type="hidden" name='inputSelectedTimeShort' value="$SelectedTimeShort">
      <input type="hidden" name='inputComments' value=" ">
      <i>*Required field</i>
    </td></tr>
  </table>
  <p><input type="submit" name="Submit" value="Check and Validate Infos" /></p>
</form>
EOT;
// ****************************************************************************
// End of form input
// ****************************************************************************
// ****************************************************************************
// End of PHP code
// ****************************************************************************
?>
</form>

<form method="post" action="AppointmentConfirmation.cgi">
<?php
	if($showSubmitbutton == false)
		echo "<input type=\"submit\" name=\"Submit\" value=\"Submit new Appointment\"  style=\"display:none;\" />";
	else if($showSubmitbutton == true)
		echo "<input type=\"submit\" name=\"Submit\" value=\"Submit new Appointment\" />";
?>
      <input type="hidden" name="inputName" value="<?=$Name; ?>"/>
      <input type="hidden" name="inputAddress" value="<?=$Address; ?>" />
      <input type="hidden" name="inputCityState" value="<?=$CityState; ?>" /> <input type="hidden" name="inputZipCode" value="<?=$ZipCode; ?>" />
      <input type="hidden" name="inputPhone" value="<?=$Phone; ?>" /> <input type="hidden" name="inputEmail" value="<?=$Email; ?>" />
      <input type="hidden" name="inputPurposeOfVisit" value="<?=$PurposeOfVisit; ?>" /><br />
	<?php 
	if(isset($_POST['inputNewPatient']))
       	echo "<input type=\"checkbox\" name=\"inputNewPatient\" checked style=\"display:none;\" />";
	else
       	echo "<input type=\"checkbox\" name=\"inputNewPatient\"  style=\"display:none;\" />";
	?>
      <!-----------------------------------------------------------------------
         Use to test if the input
        ---------------------------------------------------------------------->
      <input type="hidden" name='inputDateLong' value="<?=$DateLong; ?>" />
      <input type="hidden" name='inputDateShort' value="<?=$DateShort; ?>">
      <input type="hidden" name='inputTimeShort' value="<?=$SelectedTimeShort; ?>">
      <input type="hidden" name='inputComments' value=" ">

</form>
</fieldset>
</body>
</html>