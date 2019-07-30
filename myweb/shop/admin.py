
# Register your models here.
# shop/admin.py
from django.contrib import admin
import html
# Register your models here.
from .models import User   # 這邊一定要匯入User，感謝RelaxOP提醒
from .models import Product
from .models import Post
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

@admin.register(User)
class newUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'sex','email','phone','is_active','is_staff')
    list_filter = ('username','sex',)


@admin.register(Product)
class newProduct(admin.ModelAdmin):
	list_display = ('product_name','product_price','product_description','image_view')
	readonly_fields = ('image_view',)
	def image_view(self,obj):
		return format_html(u'<img src="%s" height="150"/>' % obj.product_image.url )
	image_view.allow_tags = True



@admin.register(Post)
class newPost(admin.ModelAdmin):
	list_display = ('post_title','post_content','post_created_at','image_vview','post_less')
	list_filter = ('post_less',)
	readonly_fields = ('image_vview',)
	def image_vview(self,obj):
		return format_html(u'<img src="%s"  height="150"/>' %obj.post_photo.url)
	image_vview.allow_tags = True

