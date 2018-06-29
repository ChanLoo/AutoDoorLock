<meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=0.5, maximum-scale=2.0, user-scalable=yes" /> 
<?php 
$order = 'sudo python close.py';
$data=shell_exec($order);
echo '请检查门是否关好！'
?>
<button   onclick="window.location.href='./open.php'">开门</button>
