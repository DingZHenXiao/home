from django.db import models

# Create your models here.
class Users(models.Model):
    # 电话号码 - CharField()
    uphone = models.CharField(max_length=11,verbose_name='电话')
    # 密码 - CharField()
    upwd = models.CharField(max_length=30,verbose_name='密码')
    # 电子邮件 - EmailField()
    uemail = models.EmailField(verbose_name='邮箱')
    # 用户名 - CharField()
    uname = models.CharField(max_length=20,verbose_name='姓名')
    # 启用/禁用 - BooleanField(),默认值为True
    isActive = models.BooleanField(default=True,verbose_name='用户状态')

    def __str__(self):
        return self.uname

    class Meta:
        db_table = "users"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

class GoodsType(models.Model):
    title = models.CharField(max_length=40)
    picture = models.ImageField(upload_to='static/upload/goodstype')
    desc = models.TextField()

    def __str__(self):
        return self.title

    def to_dict(self):
        dic = {
            "title":self.title,
            "picture":self.picture.__str__(),
            "desc":self.desc,
        }
        return dic

    class Meta:
        db_table = "goodsType"
        verbose_name = "商品类型"
        verbose_name_plural = verbose_name

# 商品 Models
class Goods(models.Model):
    title = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=7,decimal_places=2,verbose_name="价格")
    spec = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='static/upload/goods')
    isActive = models.BooleanField(default=True)
    #增加对商品类型的引用
    goodsType = models.ForeignKey(GoodsType,null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "goods"
        verbose_name = "商品"
        verbose_name_plural = verbose_name

class CarInto(models.Model):
    user = models.ForeignKey(Users)
    good = models.ForeignKey(Goods)
    ccount = models.IntegerField()

    def __str__(self):
        return "cart"

    class Meta:
        db_table = "cart"
        verbose_name = "购物车"
        verbose_name_plural = verbose_name