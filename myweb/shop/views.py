
# Create your views here.
from django.shortcuts import render
    # 在前面先引入必要的function
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from .models import Product
from .models import Post
from .models import ShoppingCar
from .form import RegisterForm
from .form import EditForm


from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import SetPasswordForm
#views.py負責接收網頁的請求(request)並回傳對應的網頁內容

# shop/views.py
def home(request):
    if (request.user.is_authenticated == True):
        mode = 1
    else:
        mode = 0
    product_list = Product.objects.all()
    post_list = Post.objects.all()
    less=[]
    for post in post_list:
        post.post_less = post.post_content[0:30]
       # less.append(post.post_content[0:30])
      #  print(post.post_less) 
    return render(request,'index.html',{'product_list':product_list, 'mode':mode, 'account': request.user.username, 'post_list':post_list})

def register(request):
	if request.method=='POST':
		form = RegisterForm(request.POST)
		print("傳送註冊資訊")
		if form.is_valid():
			new_user = form.save()
			# 如果希望註冊完馬上登入可以加入,若不需要可不加
			#--------------------------
			user_name = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user_name, password= raw_password)
			login(request,user )
			#--------------------------
			return HttpResponseRedirect('/')
	else:
		form = RegisterForm()
		print("進入註冊畫面")
	return render(request,'register.html',{'form':form,})
# 在shop/views.py 新增 User_login
def User_login(request):
    # 如果已經登入，跳至個人頁面
    # 此階段為空白頁面
    if (request.user.is_authenticated == True):
        return HttpResponseRedirect('/personal/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        # 如果User是已註冊的就login
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/') #personal
        else:
            # 如果登入失敗，則丟出錯誤訊息
            error_message = "帳號不存在或是密碼錯誤，請再試一次"
            return render(request,'login.html',{'error_message':error_message})
    return render(request,'login.html')

def personal(request):
    if not (request.user.is_authenticated == True):
        HttpResponseRedirect('/login/')
        mode = 0
    else:
        mode = 1
    instance = User.objects.get(username=request.user.username)
    if request.method =='POST':
        form =EditForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
    else:
        form =EditForm(instance=instance)

    return render(request, 'personal.html',
		{
			'account': request.user.username,
			'form':form,
            'mode':mode
		})
def User_logout(request):
	logout(request)
	return HttpResponseRedirect('/')

def reset_password(request):
    if not (request.user.is_authenticated == True):
        return HttpResponseRedirect('/login/')
    form = SetPasswordForm(user=request.user, data=request.POST)
    if form.is_valid():
        form.save()
        #update_session_auth_hash(request, form.user)
        return HttpResponseRedirect('/logout/')
    return render(request, 'reset.html',{ 'form':form })


def car(request):
    if not (request.user.is_authenticated == True):
        HttpResponseRedirect('/login/')
    user = request.user
    shopping_list = user.shoppingcar_set.all()
    if request.method == 'POST':
        booking = ShoppingCar.objects.get(pk=request.POST.get('booking_id'))
        booking.product.update_remain(-booking.count)
        booking.delete()
        HttpResponseRedirect('')
    return render(request, 'car.html', {'list':shopping_list,})

def product_detail(request, product_id):
    target = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        if not (request.user.is_authenticated == True):
            return HttpResponseRedirect('/login/')
        count = int(request.POST.get('book_count'))
        if target.update_remain(count):
            pass
        else:
            if count < 1:
                return render(request, 'detail.html',{'product': target, 'remain_code':2} )
            return render(request, 'detail.html',{'product': target, 'remain_code':1} )
        user = request.user
        booking = ShoppingCar.objects.create(client=user, product=target, count=count)
        booking.save()
    return render(request, 'detail.html',{'product': target} )

def post_detail(request, post_id):
    target = Post.objects.get(pk=post_id)
    
    return render(request, 'post/post.html',{'post': target})

def addpost(request):
    if not (request.user.is_authenticated == True):
        HttpResponseRedirect('/login/')
        mode = 0
    else:
        mode = 1
    user = request.user
     
    return render(request,'addpost.html',{ 'account': request.user.username, 'mode':mode})