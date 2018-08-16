from django.contrib import admin
from .models import *

class UsersAdmin(admin.ModelAdmin):
    list_display = ("id","uname","uphone","upwd","uemail","isActive")
    # list_display_links = ("uemail",)
    list_editable = ("uname","uphone","upwd","uemail","isActive")

class GoodsTypeAdmin(admin.ModelAdmin):
    list_display = ('id','title','picture','desc')
    # list_display_links = ('desc',)
    list_editable = ('title','picture','desc')

class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id','title','price','picture','isActive','spec')
    # list_display_links = ('spec',)
    list_editable = ('title','price','picture','isActive','spec')
    list_filter = ('goodsType',)

# Register your models here.
admin.site.register(Users,UsersAdmin)
admin.site.register(GoodsType,GoodsTypeAdmin)
admin.site.register(Goods,GoodsAdmin)
admin.site.register(CarInto)