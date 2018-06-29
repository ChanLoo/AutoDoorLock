<meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=0.5, maximum-scale=2.0, user-scalable=yes" /> 
<?php
    $userpass=array(
                    'wlx'=>'wlx1111sd',
                    'ChanLoo'=>'123456',
                    'wjw'=>'123456');
    //判断username和password是否为空
    if(!$_POST['username']|| !$_POST['upass']){
        echo '<script language="JavaScript">alert("请输入账号密码!");history.go(-1);</script>';
    }else{
    //不为空，判断密码是否正确
        $username=$_POST['username'];
        $password=$_POST['upass'];
    if($userpass[$username]==$password){
        echo"$username,你好";
    }
    else{
        echo '<script language="JavaScript">alert("帐号或密码错误!");history.go(-1);</script>';
	
        }
    }
?> 

<button   onclick="myfunction1()">开门</button>
<button   onclick="myfunction2()">关门</button>

<script language="JavaScript">


function myfunction1(){

  window.location.href='./open.php';

}
function myfunction2(){
 window.location.href='./close.php';
}

</script>



