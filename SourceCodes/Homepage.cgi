#!/usr/local/bin/php

<!--
// *************************************************************
// Project
// CSCE 4410, Summer 2012
// Student: Ka Son Chan KaSonChan@my.unt.edu
// Instructor: Don Retzlaff
// Date: August 8, 2012
//
// Homepage.cgi
// Description: Homepage.cgi is client interface homepage.
// It shows the appointment calendar to choose appointment date.
// *************************************************************
-->

<head>
<title>Welcome to Dr. Fred's Appointment Calendar</title>

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
	$showSubmitbutton = false;
?>
<fieldset>
<!--Display title-->
  <legend><p style="font-size:20pt; font-weight:bold;" align=center>
    <?php
      echo "Dr. Fred's Appointment Calendar";
    ?>
  </p></legend>
<!--End of dsiaply title-->

<!--Display subtitle-->
  <p style="font-size:16pt;" align=center>
    <?php
      echo "Select New Appointment Date";
    ?>
  </p>
<!--End of display subtitle-->

<!--Display appointment calendar-->

  <!-- element that will contain the calendar -->
  <div id="calendar-container"></div>

  <!-- Use to check selection information -->
  <div id="SelectedDate" style="text-align: center; margin-top: 0.3em"></div>

<form method="post"  action="SelectAppointmentTime.cgi">
<p align=center><input type="submit" name="Submit" value="Select Appointment Date" /></p>
  <input type="hidden" name="inputDateLong" id="SelectedDateLong" size="30" />
  <input type="hidden" name="inputDateShort" id="SelectedDateShort" size="30" />
  <input type="hidden" name="inputDay" id="SelectedDay" size="30" /><br />
</form>

<form method="post"  action="AdminHomepage.cgi">
  <p align=center><input type="submit" value="Admin Login"/><br /></p>
</form>

<script type="text/javascript">//<![CDATA[
Calendar.setup
({
    cont          : "calendar-container",
    weekNumbers   : false,
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

