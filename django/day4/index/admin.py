from django.contrib import admin
from .models import *

#声明高级管理类
class AuthorAdmin(admin.ModelAdmin):
    """docstring for AuthorAdmin"""
    #定义在列表页中要显示的字段
    list_display = ("id","name","age","email")
    list_display_links = ["email"]
    list_editable = ("age","name")



class BookAdmin(admin.ModelAdmin):
    """docstring for BookAdmin"""
    list_display = ("id","title",
        "publicate_date","publisher",)
    list_display_links = ("publicate_date",)
    list_editable = ("title","publisher",)

class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name","address","city",
        "country","website")
    list_display_links = ("country",)
    list_editable = ("name","address",
        "city","website")

class WifeAdmin(admin.ModelAdmin):
    """docstring for WifeAdmin"""
    list_display = ("name","age","author",)
    list_display_links = ("age",)
    list_editable = ("name","author",)
        

# Register your models here.
admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Wife,WifeAdmin)
