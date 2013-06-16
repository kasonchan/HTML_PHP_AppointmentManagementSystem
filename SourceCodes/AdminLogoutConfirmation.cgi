#!/usr/local/bin/php

<!--
// *************************************************************
// Project
// CSCE 4410, Summer 2012
// Student: Ka Son Chan KaSonChan@my.unt.edu
// Instructor: Don Retzlaff
// Date: August 8, 2012
//
// AdminLogout.cgi
// Description: AdminLogoutConfirmation.cgi show the logout
// screen confirmation. It redirect directly to the 
// Client Homepage.cgi.
// *************************************************************
-->

<html>
<head>
<title>Dr. Fred's Admin Appointment Calendar Admin Logout Confirmation</title>
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
      echo '<b>' . "Administration Logout" . '</b>';
    ?>
  </p>
<!--End of display subtitle-->
<!----------------------------------------------------------------------------
   Redirect back to Homepage.cgi
  ---------------------------------------------------------------------------->
<?php
echo 'You have logged out from the system.' . '<br>';
$url = 'http://students.csci.unt.edu/~kc0284/Homepage.cgi';
    echo '<META HTTP-EQUIV=Refresh CONTENT="5; URL='.$url.'">';  
?>

</fieldset>
</body>

</html>


