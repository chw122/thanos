<?php
$conn = mysqli_connect("localhost", "root", "djawleh", "emg_db");

$select_query = "SELECT value1 FROM emg_value order by num desc LIMIT 10";
$select_query2 = "SELECT value2 FROM emg_value order by num desc LIMIT 10";
$result_set = mysqli_query($conn, $select_query);
$result_set2 = mysqli_query($conn, $select_query2);
$dv = 0;
$dv2 = 0;
//$row = mysqli_fetch_array($result_set);
while( $row = mysqli_fetch_array($result_set)){
	$value[$dv] =  $row['value1'];
	$dv++ ;}

while( $row2 = mysqli_fetch_array($result_set2)){
	$value2[$dv2] =  $row2['value2'];
	$dv2++ ;}

?>
<!DOCTYPE html>
<head>
<meta charset=UTF-8" />
<meta name="robots" content="noindex,nofollow"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no"/>
<meta http-equiv="X-UA Compatible" control="IE=edge,chrome=1" />
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
<script type="text/javascript" src="./plugin/jqplot/jquery.jqplot.js"></script>
<script type="text/javascript" src="./plugin/jqplot/plugins/jqplot.canvasTextRenderer.js"></script>
<script type="text/javascript" src="./plugin/jqplot/plugins/jqplot.canvasAxisLabelRenderer.js"></script>
<link rel="stylesheet" type="text/css" href="./plugin/jqplot/jquery.jqplot.css" />
<script type="text/javascript">

$(document).ready(function(){
  // Some simple loops to build up data arrays.
  var cosPoints = [];

	cosPoints.push([0, <?php echo $value[0];?>]);
	cosPoints.push([1, <?php echo $value[1];?>]);
	cosPoints.push([2, <?php echo $value[2];?>]);
	cosPoints.push([3, <?php echo $value[3];?>]);
	cosPoints.push([4, <?php echo $value[4];?>]);
	cosPoints.push([5, <?php echo $value[5];?>]);
	cosPoints.push([6, <?php echo $value[6];?>]);
	cosPoints.push([7, <?php echo $value[7];?>]);
	cosPoints.push([8, <?php echo $value[8];?>]);
	cosPoints.push([9, <?php echo $value[9];?>]);
  
  var sinPoints = []; 
	sinPoints.push([0, <?php echo $value2[0];?>]);
	sinPoints.push([1, <?php echo $value2[1];?>]);
	sinPoints.push([2, <?php echo $value2[2];?>]);
	sinPoints.push([3, <?php echo $value2[3];?>]);
	sinPoints.push([4, <?php echo $value2[4];?>]);
	sinPoints.push([5, <?php echo $value2[5];?>]);
	sinPoints.push([6, <?php echo $value2[6];?>]);
	sinPoints.push([7, <?php echo $value2[7];?>]);
	sinPoints.push([8, <?php echo $value2[8];?>]);
	sinPoints.push([9, <?php echo $value2[9];?>]);

 
  var plot3 = $.jqplot('chart3', [cosPoints, sinPoints], 
    { 
      title:'EMG Sensor Renderer', 
      // Set default options on all series, turn on smoothing.
      seriesDefaults: {
          rendererOptions: {
              smooth: true
          }
      },
      // Series options are specified as an array of objects, one object
      // for each series.
      series:[ 
          {
            // Change our line width and use a diamond shaped marker.
            lineWidth:2, 
            markerOptions: { style:'x' }
          }, 
          {
            // Don't show a line, just show markers.
            // Make the markers 7 pixels with an 'x' style
            lineWidth:2, 
            markerOptions: { size: 7, style:"x" }
          }
      ]
    }
  );
    
});

</script>

</head>
<body>
<div id="chart3" style="height:600px;width:1200px; "></div>
<?php 
	while( $row = mysqli_fetch_array($result_set)){
		echo $row['value1'];}
?>
</body>
</html>
