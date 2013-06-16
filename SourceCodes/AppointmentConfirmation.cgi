#!/usr/local/bin/php

<!--
// *************************************************************
// Project
// CSCE 4410, Summer 2012
// Student: Ka Son Chan KaSonChan@my.unt.edu
// Instructor: Don Retzlaff
// Date: August 8, 2012
//
// AppointmentConfirmation.cgi
// Description: AppointmentConfirmation.cgi is the client 
// interface for the client to get a confirmation from the
// system after selecting date and time and inputting personal
// information in previous pages.
// It shows the client's name, appointment date and time.
// *************************************************************
-->

<!DOCTYPE html>
<html>
<head>
<title>Dr. Fred's Appointment Confirmation</title>
<meta http-equiv="Refresh" content="5;url=http://students.csci.unt.edu/~kc0284/Homepage.cgi" />
</head>
<body>

<fieldset>
<!--Display title-->
  <legend><p style="font-size:20pt; font-weight:bold;" align=center>
    <?php
      echo "Dr. Fred's Appointment Calendar";
    ?>
  </p></legend>
<!--End of dsiaply title-->

<?php
$dateToSave = $_POST["inputDateShort"];
$timeToSave = $_POST["inputTimeShort"];
$nameToSave = $_POST["inputName"];
$addressToSave = $_POST["inputAddress"];
$cityStateToSave = $_POST["inputCityState"];
$zipCodeToSave = $_POST["inputZipCode"];
$phoneToSave = $_POST["inputPhone"];
$emailToSave = $_POST["inputEmail"];
$purposeOfVisitToSave = $_POST["inputPurposeOfVisit"];
$commentsToSave = $POST["inputComments"];
if(isset($_POST["inputNewPatient"]))
  $newPatientToSave = "Yes";
else
  $newPatientToSave = "No";
// ****************************************************************************
// Use to check if the variables passing correctly from previous page
// ****************************************************************************
// echo $dateToSave . '</br>' . $timeToSave . '</br>' . $nameToSave . '</br>' . $addressToSave . '</br>' . $cityStateToSave . '</br>' . $zipCodeToSave . '</br>' . $phoneToSave . '</br>' . $emailToSave . '</br>' . $purposeOfVisitToSave . $commentsToSave . '</br>';
// echo $newPatientToSave . '</br>';

// ****************************************************************************
// Display appointment confirmation-->
// ****************************************************************************
echo 'Thank you for making appointment, ' . "<b>". $_POST["inputName"] . "</b>" . '.' . '</br>';
$dateToPrint = $_POST["inputDateLong"];
echo "Your appointment date and time is: " . "<b>" . $dateToPrint . ". </b>";
if($timeToSave == '0809')
{
  echo '<b>' . '8 am - 9 am' . '</b>' . '.' . '</br>';
  $timeToPrint = '8 am - 9 am';
}
if($timeToSave == '0910')
{
  echo '<b>' . '9 am - 10 am' . '</b>' . '.' . '</br>';
  $timeToPrint = '9 am - 10 am';
}
if($timeToSave == '1011')
{
  echo '<b>' . '10 am - 11 am' . '</b>' . '.' . '</br>';
  $timeToPrint = '10 am - 11 am';
}
if($timeToSave == '1112')
{
  echo '<b>' . '11 am - 12 pm' . '</b>' . '.' . '</br>';
  $timeToPrint = '11 am - 12 am';
}
if($timeToSave == '1213')
{
  echo '<b>' . '12 pm - 1 pm' . '</b>' . '.' . '</br>';
  $timeToPrint = '12 pm - 1 am';
}
if($timeToSave == '1314')
{
  echo '<b>' . '1 pm - 2 pm' . '</b>' . '.' . '</br>';
  $timeToPrint = '1 pm - 2 pm';
}
if($timeToSave == '1415')
{
  echo '<b>' . '2 pm - 3 pm' . '</b>' . '.' . '</br>';
  $timeToPrint = '2 pm - 3 pm';
}
if($timeToSave == '1516')
{
  echo '<b>' . '3 pm - 4 pm' . '</b>' . '.' . '</br>';
  $timeToPrint = '3 pm - 4 pm';
}
if($timeToSave == '1617')
{
  echo '<b>' . '4 pm - 5 pm' . '</b>' . '.' . '</br>';
  $timeToPrint = '4 pm - 5 pm';
}
// ****************************************************************************
// End of display appointment confirmation-->
// ****************************************************************************

// ****************************************************************************
// Send email to the patient with provided email
// ****************************************************************************
if($emailToSave != "")
{
  echo "A confirmation email has been sent to your email." . '</br>';

  $to = $emailToSave;
  $subject = "Dr. Fred's Appointment Confirmation";
  $message = 'Thank you for making appointment, ' . $nameToSave . '.' . "\n" . 'Your appointment date and time is: ' . $dateToPrint . '. ' . $timeToPrint . '.' . "\n\n" . 'Dr. Fred' . "\n" . '1155 Union Circle' . "\n" . 'Denton, TX 76203' . "\n" . '9405652000' . "\n";
  mail($to,$subject,$message);
}
// ****************************************************************************
// End of send email to the patient with provided email
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
  if($date == $dateToSave)
    $dateExisted = 'true';
  // echo "$date<br />\n";
  foreach ($dArray as $time => $tArray)
  {
    // echo "$time<br/>\n";
    foreach ($tArray as $field => $info)
    {
      // echo "$field => $info<br />\n";
      $PersonalInfoArray[$field] = $info;
    }
  }
}
}
// ****************************************************************************
// End of reading the whole data file to inputInfo array
// ****************************************************************************

// ****************************************************************************
// Add the new client info and write to the datafile
// ****************************************************************************
$PersonalInfoArray = array ('Name' => $nameToSave, 'Address' => $addressToSave, 'City/State' => $cityStateToSave, 'ZipCode' => $zipCodeToSave, 'Phone' => $phoneToSave, 'Email' => $emailToSave, 'PurposeOfVisit' => $purposeOfVisitToSave, 'NewPatient' => $newPatientToSave, 'Comments' => "No comments.");
if($dateExisted == 'false')
{
  $TimeArray = array ($timeToSave => $PersonalInfoArray);
  $infos[$dateToSave] = $TimeArray;
}
else
{
  $TimeArray = array ($timeToSave => $PersonalInfoArray);
  $infos["$dateToSave"]["$timeToSave"] = $PersonalInfoArray;
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
?>

</fieldset>
</body>
</html>