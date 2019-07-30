# shop/form.py
from django.forms import ModelForm
from .models import User
from django.contrib.auth.forms import UserCreationForm

#Register繼承了UserCreationForm，因為Django原本的UserCreationForm只有username跟password1(密碼)及password2(密碼確認)，
#為了新增其他的欄位，我們新增RegisterForm，如何顯示label，或是決定要出現哪些欄位，都可以從這裡調整。
class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        # 要override password1,2 的label必須要從這裡改
        self.fields['password1'].label = "密碼"
        self.fields['password2'].label = "密碼確認"
    class Meta:
        model = User
        # 決定註冊欄位要有哪些及順序
        fields = ('username','password1','password2','name','sex','phone')
        # 各欄位顯示的標籤，如沒有則就是原本的變數名稱
        labels = {
            "username": "帳號",
            "name":"姓名",
            "sex":"性別",
            "phone":"手機",
        }

class EditForm(ModelForm):
    """docstring for ClassName"""
    class Meta:
        model = User 
        fields = ('username','name','sex','email','phone')
        labels = {
            "username": "帳號",
            "name":"姓名",
            "sex":"性別",
            "phone":"手機",
            "email":"信箱",
        }    
# class EditForm(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#         super(EditForm, self).__init__(*args, **kwargs)
#         # 要override password1,2 的label必須要從這裡改
#         #del self.fields['password1']
#         #del self.fields['password2']
#         self.fields['password1'].label = "密碼"
#         self.fields['password2'].label = "密碼確認"
#     class Meta:
#         model = User
#         # 決定註冊欄位要有哪些及順序
#         fields = ('name','sex','email','phone')
#         # 各欄位顯示的標籤，如沒有則就是原本的變數名稱
#         labels = {
#             "username": "帳號",
#             "name":"姓名",
#             "sex":"性別",
#             "phone":"手機",
#             "email":"信箱",
#         }
