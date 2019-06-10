<?php
$conn = mysqli_connect("localhost", "root", "djawleh", "emg_db");
//DB연결
$select_query = "SELECT value1 FROM emg_value order by num desc LIMIT 10";
$select_query2 = "SELECT value2 FROM emg_value order by num desc LIMIT 10";
//DB에서 근전도 센서 값 2개를 최대 10개까지만 불러오는 query문
$result_set = mysqli_query($conn, $select_query);
$result_set2 = mysqli_query($conn, $select_query2);
//query문 실행
$dv = 0;
$dv2 = 0;
//$row = mysqli_fetch_array($result_set);
while( $row = mysqli_fetch_array($result_set)){
	$value[$dv] =  $row['value1'];
	//받아온 값을 새로 선언한 배열에 저장
	$dv++ ;}

while( $row2 = mysqli_fetch_array($result_set2)){
	$value2[$dv2] =  $row2['value2'];
	$dv2++ ;}
//PHP코드 끝
?>
<!DOCTYPE html>
<head>
<meta charset=UTF-8" />
<meta name="robots" content="noindex,nofollow"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no"/>
<meta http-equiv="X-UA Compatible" control="IE=edge,chrome=1" />
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
<!-- jquery import-->
<script type="text/javascript" src="./plugin/jqplot/jquery.jqplot.js"></script>
<script type="text/javascript" src="./plugin/jqplot/plugins/jqplot.canvasTextRenderer.js"></script>
<script type="text/javascript" src="./plugin/jqplot/plugins/jqplot.canvasAxisLabelRenderer.js"></script>
<link rel="stylesheet" type="text/css" href="./plugin/jqplot/jquery.jqplot.css" />
<!--그래프를 그리는데 필요한 jquery library를 import함-->
<script type="text/javascript">
<!--javascript로 그래프 부분을 코딩함-->
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
	// php를 이용해 받아온 DB값을 그래프로 올려줌
  
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
	// php를 이용해 받아온 DB값을 그래프로 올려줌

 
  var plot3 = $.jqplot('chart3', [cosPoints, sinPoints], //차트 이름과 그래프를 그릴 값을 지정
    { 
      title:'EMG Sensor Renderer', 
      // Set default options on all series, turn on smoothing.
      seriesDefaults: {
          rendererOptions: {
              smooth: true
          }
	// 그래프에서 필요한 값을 초기화 해줌(제목, 그래프 스타일)
      },
      // Series options are specified as an array of objects, one object
      // for each series.
      series:[ 
          {
            // Change our line width and use a diamond shaped marker.
            lineWidth:2, 
            markerOptions: { style:'x' }
          }, 
	//그래프에 그려질 선의 스타일을 지정
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
<!--세로600, 가로 1200의 크기로 그래프 출력-->
</body>
</html>
