#!/usr/local/bin/php

<html>

<head>
<title>Testing</title>

<!--Calendar script-->

<!--End of calendar script-->
</head>

<body>

<?php

$infos = array (
  '20120813' => array (
    '0809' => array (
      'Name' => 'Stephen Moon',
      'Address' => '1155 Union Circle',
      'City/State' => 'Denton, TX',
      'ZipCode' => 76211,
      'Phone' => 940562000,
      'Email' => 'stephen.moon@my.unt.edu',
      'PurposeOfVisit' => 'Sore throat.',
      'NewPatient' => 'Yes',
    ),
    '1314' => array (
      'Name' => 'Louis Wu',
      'Address' => '425 Bernard Street',
      'City/State' => 'Denton, TX',
      'ZipCode' => 78751,
      'Phone' => 5129199242,
      'Email' => 'louius.wu@my.unt.edu',
      'PurposeOfVisit' => 'Headache.',
      'NewPatient' => 'No',
    ),
  ),
);

foreach ($infos as $date => $dArray)
{
  echo "$date<br />\n";
  foreach ($dArray as $time => $tArray)
  {
    echo "$time<br/>\n";
    foreach ($tArray as $field => $info)
      echo "$field => $info<br />\n";
  }
}

?>

<?php
// Convert the data into a PHP compatible data stream
$data = "<?php\n\$infos = " . var_export($infos,true) . ";\n?" . ">\n";

// Write the data to a file
$fh = fopen('datafile.dat','w');
fputs ($fh,$data);
fclose ($fh);


$inputInfos = array();
$inputInfos = include 'datafile.dat';
echo "Reading...<br/>\n";

foreach ($infos as $date => $dArray)
{
  echo "$date<br />\n";
  foreach ($dArray as $time => $tArray)
  {
    echo "$time<br/>\n";
    foreach ($tArray as $field => $info)
      echo "$field => $info<br />\n";
  }
}



?>


END!

</body>

</html>


