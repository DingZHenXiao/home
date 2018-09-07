$(function(){
    $("#formReg").submit(function(){
        if($("#upwd").val() != $("#cpwd").val()){
            console.log("两次密码不一致")
            return false;
        }
    })
    
})