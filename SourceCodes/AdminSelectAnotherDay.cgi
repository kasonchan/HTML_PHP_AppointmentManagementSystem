#!/usr/local/bin/php

<!--
// *************************************************************
// Project
// CSCE 4410, Summer 2012
// Student: Ka Son Chan KaSonChan@my.unt.edu
// Instructor: Don Retzlaff
// Date: August 8, 2012
//
// AdminSelectAnotherDay.cgi
// Description: AdminSelectAnotherDay.cgi let the admins to 
// update client's appointment date and time.
// It shows all the calendar
// *************************************************************
-->

<html>

<head>
<!--Calendar script-->
    <link rel="stylesheet" type="text/css" href="jscal2.css" />
    <link rel="stylesheet" type="text/css" href="border-radius.css" />
    <link rel="stylesheet" type="text/css" href="steel.css" />
    <script type="text/javascript" src="jscal2.js"></script>
    <script type="text/javascript" src="en.js"></script>
<!--End of calendar script-->
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
$oldTime = substr($updateTime, 0, 2) . substr($updateTime, 2, 2);
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
	echo "Select another date for Appointment";
	echo '<b>' . date(" l, F j, Y", mktime(0, 0, 0, $month, $day, $year)) . ' ' . $timeSlot . '</b>' . '.' . '<br>';
    ?>
  </p>
<!----------------------------------------------------------------------------
   End of display subtitle
  ---------------------------------------------------------------------------->
<!--Display appointment calendar-->

  <!-- element that will contain the calendar -->
  <div id="calendar-container"></div>

  <!-- Use to check selection information -->
  </div><div id="SelectedDate" style="text-align: center; margin-top: 0.3em"></div>

<!----------------------------------------------------------------------------
   Display the calendar
  ---------------------------------------------------------------------------->
<form method="post" action="AdminSelectAnotherDayConfirmation.cgi">
      <input type="hidden" name="inputName" value="<?=$_POST['inputName']; ?>"/><br>
      <input type="hidden" name="inputAddress" value="<?=$_POST['inputAddress']; ?>" /><br>
      <input type="hidden" name="inputCityState" value="<?=$_POST['inputCityState']; ?>" /><input type="hidden" name="inputZipCode" value="<?=$_POST['inputZipCode']; ?>" />
      <input type="hidden" name="inputPhone" value="<?=$_POST['inputPhone']; ?>" /><input type="hidden" name="inputEmail" value="<?=$_POST['inputEmail']; ?>" />
      <input type="hidden" name="inputPurposeOfVisit" value="<?=$_POST['inputPurposeOfVisit']; ?>" />
      <textarea name="inputComments" rows=0 cols=0 style="visibility:hidden;"><?=$_POST['inputComments']; ?></textarea>
  
  <input type="hidden" name="oldDateShort" value="<?=$_POST['outputDateShort']; ?>" />
  <input type="hidden" name="oldTimeShort" value="<?=$oldTime; ?>" />
  
  <input type="hidden" name="newDateLong" id="SelectedDateLong" size="30" />
  <input type="hidden" name="newDateShort" id="SelectedDateShort" size="30" />
  
  <input type="hidden" name="inputDay" id="SelectedDay" size="30" /><br />
  <p align=center><input type="submit" value="Select new Appointment Date"/><br /></p>
</form>

<script type="text/javascript">//<![CDATA[
Calendar.setup
({
    cont          : "calendar-container",
    weekNumbers   : true,
    selectionType : Calendar.SEL_SINGLE,
    selection     : Calendar.dateToInt(new Date()),
    showTime      : false,
    onSelect      : function(cal) {
        var count = this.selection.countDays();
        if (count == 1) {
            var date = this.selection.get();
            date = Calendar.intToDate(date);

            // Get the selected date in short form YYYYMMDD i.e. 20121201
            document.getElementById("SelectedDateShort").innerHTML = Calendar.dateToInt(date);
            SelectedDateShort.value = Calendar.dateToInt(date);
            // alert(Calendar.dateToInt(date));

            // Get the selected date in long form with day i.e. Monday, August 23, 2012
            document.getElementById("SelectedDay").innerHTML = Calendar.printDate(date, "%A");
            SelectedDay.value = Calendar.printDate(date, "%A");

            // Get the selected day i.e. Monday
            date = Calendar.printDate(date, "%A, %B %d, %Y");
            document.getElementById("SelectedDate").innerHTML = date;
            document.getElementById("SelectedDateLong").innerHTML = date;
            SelectedDateLong.value = date;

            $("calendar-info").innerHTML = date;
        } else {
            $("calendar-info").innerHTML = Calendar.formatString(
                "${count:no date|one date|two dates|# dates} selected",
                { count: count }
            );
        }
    },
    disabled: function(date) {
        if (date.getDay() == 0 || date.getDay() == 6) {
            return true;
        } else {
            return false;
        }
    }
});
//]]></script>

<!--End of display appointment calendar-->

</fieldset>
</body>

</html>

