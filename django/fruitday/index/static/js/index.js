$(function () {
  loadGoods();
  check_login();
});

function loadGoods() {
  $.get("/all_type_goods/",function(data){
    var show = "";
    $.each(data,function(i,obj){
      var html = "<div class='item'>";
      //将obj.type转换为json对象后取值
      var jsonType = JSON.parse(obj.type);
        html += "<p class='title'>";
          html += "<a href='#'>更多</a>";
          html += "<img src='/"+jsonType.picture+"'>";
        html += "</p>";
        html += "<ul>";
        var jsonGoods = JSON.parse(obj.goods);
        //循环遍历jsonGoods中的每一项内容，构建li
        $.each(jsonGoods,function(j,good){
          if((j+1)%5==0){
            html += "<li class='no-margin'>";
          }else{
            html += "<li>";
          }
            html += "<p>";
              html += "<img src='/"+good.fields.picture+"'>";
            html += "</p>";
            html += "<div class='content'>";
              html+= "<a href='javascript:add_cart("+good.pk+");' class='cart'>";
                html += "<img src='/static/images/cart.png'>";
              html += "</a>";
              html += "<p>";
                html += good.fields.title;
              html += "</p>";
              html += "<span>";
                html += '&yen;';
                html+= good.fields.price;
              html += "</span>";
            html += "</div>";
          html += "</li>";
        });
        html += "</ul>";
      html += "</div>";
      show += html;
    });
    $("#main").html(show);
  },"json");
}

function check_login(){
  $.get("/check_login/",function(data){
    var html = "";
    if(data.loginStatus==0){
      html+="<a href='/login/'>[登录]</a>";
      html+="<a href='/register/'>注册有惊喜</a>";
    }
    else{
      html+="欢迎:"+data.uname;
      html+="&nbsp;&nbsp;&nbsp;&nbsp;";
      html+="<a href='/logout/'>退出</a>";
    }
    $("#login-info").html(html);
  },"json");
}

// 添加商品至购物车
function add_cart(good_id){
  // alert("购买的商品的ID:"+goods_id);
  //验证是否有用户处于登录状态,如果未处于登录状态，则给出提示，否则将信息传递给后台服务器
  $.get("/check_login/",function(data){
    if(data.loginStatus==0){
      alert("请先登录...");
    }
    else{
      // alert('允许将商品加入至购物车');
      $.post("/add_cart/",{'good_id':good_id,
        "csrfmiddlewaretoken":$.cookie('csrftoken'),},function (data) {
      if(data.status==1){
        alert("添加购物车成功")
      }
      else{
        alert('添加购物车失败')
      }
      },"json");
    }
  },"json");
}