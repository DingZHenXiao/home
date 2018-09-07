from django import forms
from .models import *

TOPIC_CHOICE = (
    ("level1", "好评"),
    ("level2", "中评"),
    ("level3", "差评"),
)


class RemarkForm(forms.Form):
    """docstring for ClassName"""
    subject = forms.CharField(label="标题")
    email = forms.EmailField(label="邮箱")
    message = forms.CharField(label="内容",
                              widget=forms.Textarea)
    topic = forms.ChoiceField(label="评论",
                              choices=TOPIC_CHOICE)
    isSvsed = forms.BooleanField(label="是否保存")

# class RegisterForm(forms.Form):
#     uname = forms.CharField(label="用户名称")
#     upwd = forms.CharField(label="用户密码",
#                            widget=forms.PasswordInput)
#     uemail = forms.EmailField(label="用户邮箱")
#     uage = forms.IntegerField(label="用户年龄")


class RegisterForm(forms.ModelForm):
    # 创建Meta内部类，关联Models
    class Meta:
        # 制定关联的model类
        model = Users
    # 指定要生成的控件
        fields = "__all__"
    # 指定每个控件对应的label
        labels = {
            "uname": "用户名称",
            "upwd": "用户密码",
            "uemail": "用户邮箱",
            "uage": "用户年龄",
        }


class LoginForm(forms.ModelForm):
    # 创建Meta内部类
    class Meta:
        # 指定要关联的Models类
        model = Users
        # 指定要生成的控件
        fields = ["uname", "upwd"]
        # 指定要生成的名称
        labels = {
            "uname": "用户名称",
            "upwd": "用户密码",
        }


class WidForm2(forms.ModelForm):
    class Meta:
        #制定实体
        model = Users
        #指定字段
        fields = ['uname','upwd']
        #指定字段标签
        labels = {
                'uname':'用户名称',
                'upwd': '用户密码',
        }
        #制定字段小部件
        widgets = {'uname': forms.TextInput(
            attrs={'placeholder': '6-20位的用户名'}),
                    'upwd': forms.PasswordInput(
                        attrs={'placeholder': '6-18位密码'})}
            
#     uname = forms.CharField(label="用户名称"，widget=forms.TextInput(
#         attrs={'placeholder': '用户名称', 'class': 'form-control',}))
#     upwd = forms.CharField(label="用户密码", widget=forms.PasswordInput(
#         attrs={'placeholder': '用户密码',}))
