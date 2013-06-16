#!/usr/local/bin/php

<!--
// *************************************************************
// Project
// CSCE 4410, Summer 2012
// Student: Ka Son Chan KaSonChan@my.unt.edu
// Instructor: Don Retzlaff
// Date: August 8, 2012
//
// AdminHomepage.cgi
// Description: AdminHomepage.cgi shows the login screen
// for the administration to log in the system.
// *************************************************************
-->

<html>

<head>
<title>Dr. Fred's Admin Appointment Calendar Admin Login</title>
</head>

<body>
<fieldset>
<!--Display title-->
  <legend><p style="font-size:20pt; font-weight:bold;" align=center>
    <?php
      echo "Dr. Fred's Admin Appointment Calendar";
    ?>
  </p></legend>
<!--End of dsiaply title-->

<!--Display subtitle-->
  <p style="font-size:16pt;">
    <?php
      echo '<b>' . "Administration Login" . '</b>';
    ?>
  </p>
<!--End of display subtitle-->

<?php
if (count($_POST) > 0) 
{ // process the submitted form
  // do some simple field checking first...
  
  // make certain something is entered in the username and password field
  if (trim($Username=$_POST['username']) != 'admin' || trim($Password=$_POST['password']) != 'admin')
  {
    $error = true;
    echo "<div style=\"color:red;\">Your Login ID does not exist and/or password is incorrect.</div>\n";
  }

  if (!$error)
  {
    $url = 'http://students.csci.unt.edu/~kc0284/AdminUpdateCalendar.cgi';
    echo '<META HTTP-EQUIV=Refresh CONTENT="0; URL='.$url.'">';  
  }
}
// ****************************************************************************
// End of form validation
// ****************************************************************************
// ****************************************************************************
// Login form
// ****************************************************************************
if ($error OR count($_POST) == 0)
  echo <<< EOT
<form id='login' action='' method='post'>
<input type='hidden' name='submitted' id='submitted' value='1'/>
<label for='username' >Login ID:</label>
<input type='text' name='username' id='username'/></br>
<label for='password' >Password:</label>
<input type='password' name='password' id='password'/></br>
<p><input type='submit' name='Login' value='Login' /></p>
</form>
EOT;
// ****************************************************************************
// End of login form
// ****************************************************************************
?>

</fieldset>
</body>

</html>


