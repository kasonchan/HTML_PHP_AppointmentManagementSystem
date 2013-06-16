#!/usr/local/bin/php

<!--
// *************************************************************
// Project
// CSCE 4410, Summer 2012
// Student: Ka Son Chan KaSonChan@my.unt.edu
// Instructor: Don Retzlaff
// Date: August 8, 2012
//
// AdminWeekAppointmendSchedule.cgi
// Description: AdminWeekAppointmendSchedule.cgi is the admin 
// interface for the admin to edit infos, delete appointments,
// select another date of the client appointments.
// It shows the week calendar from the selected day from
// AdminUpdateCalendar.cgi with time slots and client names.
// *************************************************************
-->

<html>
<head>
<title>Dr. Fred's Admin Appointment Week Appointment Schedule</title>
<!--Calendar script-->

<!--End of calendar script-->
</head>

<body>
<?php
    // ************************************************************************
    // Use to test if variables values pass from previous page 
    // ************************************************************************
    $Day = $_POST["inputDay"];
    $SelectedDayLong = $_POST["inputDateLong"];
    $SelectedDayShort = $_POST["inputDateShort"];
    $month = substr($SelectedDayShort, 4, 2);
    $day = substr($SelectedDayShort, 6, 2);
    $year = substr($SelectedDayShort, 0, 4);
    $fullDay = date("l", mktime(0, 0, 0, $month, $day, $year));
    $firstDay; $firstMonth; $firstYear;
    // echo $Day . "<br>" . $SelectedDayLong . "<br>" . $SelectedDayShort . "<br>";
    // echo $month . " " . $day . " " . $year . "<br>";
    // echo $fullDay;
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
      echo "Appointment Schedule for the week " . '<b>' . $SelectedDayLong . '</b>' . '.' . '<br>';
      returnFirstDate($firstDay, $firstMonth, $firstYear, $day, $month, $year);
      // Use to test if the return First Date running correctly
      // echo $firstDay . ' ' . $firstMonth . ' ' . $firstYear . '<br>';
    ?>
  </p>
<!----------------------------------------------------------------------------
   End of display subtitle
  ---------------------------------------------------------------------------->

<form action="AdminUpdateCalendar.cgi">
<?php
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
		echo "<div style=\"color:red;\">No week was selected.</div>\n";
	}

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
	<input type="submit" name="Submit" value="Submit new Appointment week" />
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




<!----------------------------------------------------------------------------
   Display appointment schedule in week form
  ---------------------------------------------------------------------------->
<form method='post' action="AdminUpdateAppointment.cgi">
<table frame='border' border=1>
<!-----Title row----->
<tr>
  <td></td>
  <td><?php echo date("l F j", mktime(0, 0, 0, $firstMonth, $firstDay, $firstYear)); ?></td>
  <td><?php echo date("l F j", mktime(0, 0, 0, $firstMonth, $firstDay + 1, $firstYear)); ?></td>
  <td><?php echo date("l F j", mktime(0, 0, 0, $firstMonth, $firstDay + 2, $firstYear)); ?></td>
  <td><?php echo date("l F j", mktime(0, 0, 0, $firstMonth, $firstDay + 3, $firstYear)); ?></td>
  <td><?php echo date("l F j", mktime(0, 0, 0, $firstMonth, $firstDay + 4, $firstYear)); ?></td>
</tr>
<!-----1st row 0809----->
<tr>
  <td>8-9</td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay, $firstYear)), '0809'); echo '<input type=radio name=SelectedDateTime value=00809 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 1, $firstYear)), '0809'); echo '<input type=radio name=SelectedDateTime value=10809 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 2, $firstYear)), '0809'); echo '<input type=radio name=SelectedDateTime value=20809 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 3, $firstYear)), '0809'); echo '<input type=radio name=SelectedDateTime value=30809 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 4, $firstYear)), '0809'); echo '<input type=radio name=SelectedDateTime value=40809 />'; ?></td>
</tr>
<!-----2nd row 0910----->
<tr>
  <td>9-10</td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay, $firstYear)), '0910');  echo '<input type=radio name=SelectedDateTime value=00910 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 1, $firstYear)), '0910');  echo '<input type=radio name=SelectedDateTime value=10910 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 2, $firstYear)), '0910');  echo '<input type=radio name=SelectedDateTime value=20910 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 3, $firstYear)), '0910');  echo '<input type=radio name=SelectedDateTime value=30910 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 4, $firstYear)), '0910');  echo '<input type=radio name=SelectedDateTime value=40910 />'; ?></td>
</tr>
<!-----3rd row 1011----->
<tr>
  <td>10-11</td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay, $firstYear)), '1011');  echo '<input type=radio name=SelectedDateTime value=01011 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 1, $firstYear)), '1011');  echo '<input type=radio name=SelectedDateTime value=11011 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 2, $firstYear)), '1011');  echo '<input type=radio name=SelectedDateTime value=21011 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 3, $firstYear)), '1011');  echo '<input type=radio name=SelectedDateTime value=31011 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 4, $firstYear)), '1011');  echo '<input type=radio name=SelectedDateTime value=41011 />'; ?></td>
</tr>
<!-----4th row 1112----->
<tr>
  <td>11-12</td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay, $firstYear)), '1112');  echo '<input type=radio name=SelectedDateTime value=01112 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 1, $firstYear)), '1112');  echo '<input type=radio name=SelectedDateTime value=11112 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 2, $firstYear)), '1112');  echo '<input type=radio name=SelectedDateTime value=21112 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 3, $firstYear)), '1112');  echo '<input type=radio name=SelectedDateTime value=31112 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 4, $firstYear)), '1112');  echo '<input type=radio name=SelectedDateTime value=41112 />'; ?></td>
</tr>
<!-----5th row 1213----->
<tr>
  <td>12-1</td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay, $firstYear)), '1213');  echo '<input type=radio name=SelectedDateTime value=01213 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 1, $firstYear)), '1213');  echo '<input type=radio name=SelectedDateTime value=11213 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 2, $firstYear)), '1213');  echo '<input type=radio name=SelectedDateTime value=21213 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 3, $firstYear)), '1213');  echo '<input type=radio name=SelectedDateTime value=31213 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 4, $firstYear)), 1213);  echo '<input type=radio name=SelectedDateTime value=41213 />'; ?></td>
</tr>
<!-----6th row 1314----->
<tr>
  <td>1-2</td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay, $firstYear)), '1314');  echo '<input type=radio name=SelectedDateTime value=01314 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 1, $firstYear)), '1314');  echo '<input type=radio name=SelectedDateTime value=11314 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 2, $firstYear)), '1314');  echo '<input type=radio name=SelectedDateTime value=21314 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 3, $firstYear)), '1314');  echo '<input type=radio name=SelectedDateTime value=31314 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 4, $firstYear)), '1314');  echo '<input type=radio name=SelectedDateTime value=41314 />'; ?></td>
</tr>
<!-----7th row 1415----->
<tr>
  <td>2-3</td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay, $firstYear)), '1415');  echo '<input type=radio name=SelectedDateTime value=01415 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 1, $firstYear)), '1415');  echo '<input type=radio name=SelectedDateTime value=11415 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 2, $firstYear)), '1415');  echo '<input type=radio name=SelectedDateTime value=21415 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 3, $firstYear)), '1415');  echo '<input type=radio name=SelectedDateTime value=31415 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 4, $firstYear)), '1415');  echo '<input type=radio name=SelectedDateTime value=41415 />'; ?></td>
</tr>
<!-----8th row 1516----->
<tr>
  <td>3-4</td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay, $firstYear)), '1516');  echo '<input type=radio name=SelectedDateTime value=01516 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 1, $firstYear)), '1516');  echo '<input type=radio name=SelectedDateTime value=11516 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 2, $firstYear)), '1516');  echo '<input type=radio name=SelectedDateTime value=21516 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 3, $firstYear)), '1516');  echo '<input type=radio name=SelectedDateTime value=31516 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 4, $firstYear)), '1516');  echo '<input type=radio name=SelectedDateTime value=41516 />'; ?></td>
</tr>
<!-----9th row 1617----->
<tr>
  <td>4-5</td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay, $firstYear)), '1617');  echo '<input type=radio name=SelectedDateTime value=01617 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 1, $firstYear)), '1617');  echo '<input type=radio name=SelectedDateTime value=11617 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 2, $firstYear)), '1617');  echo '<input type=radio name=SelectedDateTime value=21617 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 3, $firstYear)), '1617');  echo '<input type=radio name=SelectedDateTime value=31617 />'; ?></td>
  <td><?php getName(date("Ymd", mktime(0, 0, 0, $firstMonth, $firstDay + 4, $firstYear)), '1617');  echo '<input type=radio name=SelectedDateTime value=41617 />'; ?></td>
</tr>
</table>
<input type='hidden' name="inputDateShort" value=<?=$SelectedDayShort; ?> >
<input type='hidden' name="inputDateLong" value=<?=$SelectedDayLong; ?> >
<p><input type="submit" name="SubmitNewAppointment" value="Edit Selected Appointment" />

<input type="submit" name="SelectAnotherDay" value="Select Another Date" />
<input type="submit" name="DeleteSelectedAppointment" value="Delete Selected Appointment" action="AdminDeleteAppointment.cgi" />
</p>
</form>
<!----------------------------------------------------------------------------
   Logout button
  ---------------------------------------------------------------------------->
<form action="AdminLogoutConfirmation.cgi">
   <p><input type="submit" name="Logout" value="Logout" /></p>
</form>
<!----------------------------------------------------------------------------
   End of display appointment schedule in week form
  ---------------------------------------------------------------------------->

<?php
// ****************************************************************************
// Function Definitions
// ****************************************************************************
// Testing code for getName function
// getName(20120813, 1112);
/*
	// Test code to get date
	$date = date($year . '-' . $month . '-' . $day);
	// echo 'current date: ' . $date . '<br>';
	$date = date("Y-m-d", strtotime($date) . " +1 day");
	echo $date . '<br>';
	echo substr($date, 0, 4) . '<br>';
	echo substr($date, 5, 2) . '<br>';
	echo substr($date, 8, 2) . '<br>';
*/

// addDay($firstDay, $firstMonth, $firstYear, $calDay, $calMonth, $calYear, 1);
// echo $calDay . ' ' . $calMonth . ' ' . $calYear . '<br>';

function returnFirstDate(&$firstDay, &$firstMonth, &$firstYear, $day, $month, $year)
{
	if(date("l", mktime(0, 0, 0, $month, $day, $year)) == "Monday")
	{
		$firstDay = $day;
		$firstMonth = $month;
		$firstYear = $year;
	}
	else if(date("l", mktime(0, 0, 0, $month, $day, $year)) == "Saturday")
	{
		$ToFixDate = date($year . '-' . $month . '-' . $day);
		$ToFixDate = date('Y-m-d', strtotime('+2 days')) . '<br>';
		$firstDay = substr($ToFixDate, 8, 2);
		$firstMonth = substr($ToFixDate, 5, 2);
		$firstYear = substr($ToFixDate, 0, 4);
	}
	else if(date("l", mktime(0, 0, 0, $month, $day, $year)) == "Sunday")
	{
		$ToFixDate = date($year . '-' . $month . '-' . $day);
		$ToFixDate = date('Y-m-d', strtotime('+1 day')) . '<br>';
		$firstDay = substr($ToFixDate, 8, 2);
		$firstMonth = substr($ToFixDate, 5, 2);
		$firstYear = substr($ToFixDate, 0, 4);
	}
}

function getName($checkDate, $checkTime)
{
	$inputInfos = array();
	if(file_exists('datafile.dat'))
  	{
    		$inputInfos = include 'datafile.dat';
		foreach ($infos as $date => $dArray) 
		{
  			if($checkDate == $date)
  			foreach ($dArray as $time => $tArray) 
			{
				if($checkTime == $time)
    				foreach ($tArray as $field => $info)
				if($field == "Name")
				{
					echo $info;
				}
  			}
		}
	}
}
// ****************************************************************************
// End of function Definitions
// ****************************************************************************
?>

</fieldset>
</body>

</html>

