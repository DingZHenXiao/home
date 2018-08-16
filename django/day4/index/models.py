from django.db import models

# Create your models here.
class Publisher(models.Model):
    """docstring for Publisher"""
    name=models.CharField(max_length=30,
        verbose_name="姓名")
    address=models.CharField(max_length=50,
        verbose_name="地址")
    city=models.CharField(max_length=20,
        verbose_name="城市")
    country=models.CharField(max_length=20,
        verbose_name="国家")
    website=models.URLField(verbose_name="网址")

    def __str__(self):
        return self.name
    class Meta:
        db_table = "publisher"
        verbose_name = "出版社"
        verbose_name_plural = verbose_name
        ordering = ["id"]
            
class AuthorManager(models.Manager):
    #添加自定义函数
    def auCount(self):
        return self.all().count()

    def ltAge(self,age):
        return self.filter(age__lt=age)

class Author(models.Model):
    #使用AuthorManager覆盖objects
    objects = AuthorManager()
    """docstring for Author"""
    name=models.CharField(max_length=20,
        verbose_name='姓名')
    age=models.CharField(max_length=20,
        verbose_name='年龄')
    email=models.CharField(max_length=20,
        verbose_name='邮箱')
    isActive=models.BooleanField(default=True)
    publisher = models.ManyToManyField(Publisher)

    def __str__(self):
        return self.name
    class Meta:
        #1　指定表明
        db_table="author"
        #2.指定显示的中文名
        verbose_name='作者'
        #3.指定显示的中文名(复数)
        verbose_name_plural = verbose_name
        #4.指定降序
        ordering = ['id']

class BookManager(models.Manager):
    def title_count(self,keywords):
        return self.filter(title__contains=
            keywords)

class Book(models.Model):
    """docstring for Book"""
    objects = BookManager()
    title=models.CharField(max_length=20,
        verbose_name="书名") 
    publicate_date=models.DateField(
        verbose_name="出版日期")
    #增加对publisher的引用（一对多）
    publisher = models.ForeignKey(Publisher,
        null=True)
    author = models.ManyToManyField(Author)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "book"
        verbose_name = "图书"
        verbose_name_plural = verbose_name
        ordering = ["id"]

class Wife(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    #一对一映射，引用自author实体
    author = models.OneToOneField(Author)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "wife"
        verbose_name = "夫人"
        verbose_name_plural = verbose_name