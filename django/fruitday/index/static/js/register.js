$(function(){
    //为　#formReg 绑定　submit 事件
    $("#formReg").submit(function(){
        if($("#upwd").val() != $('#cpwd').val()){
            alert('两次密码不一致，请重新输入')
            return false;
        }
        if($("#uphone-show").html()=="手机已经被注册"){
            return false;
        }
        if($("#uphone-show").html()=="手机号不正确"){
            return false;
        }
        return true;
    });
    $("input[name='uphone']").blur(function(){
        check_phone();
    });
});

function check_phone(){
    $.get('/checkphone/',"uphone="+$("input[name='uphone']").val(),
      function(data){$("#uphone-show").html(data.msg);},"json"
    );
};