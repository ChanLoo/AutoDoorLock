<meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=0.5, maximum-scale=2.0, user-scalable=yes" /> 

<?php 
$order = 'sudo python open.py';
$data=shell_exec($order);
echo "请进！"
?>
<button   onclick="window.location.href='./close.php'">关门</button>
