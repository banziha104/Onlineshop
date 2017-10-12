from django.contrib import admin
from .models import Category,Product
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)} # name을 기준으로 자동으로 생성해라
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','category','price','stock','available','created','updated']
    list_filter =  ['available','created','updated','category'] # 우측생성 되는 필터
    list_editable = ['price','stock','available']               # 수정으로 들어가지 않더라도 목록에서 수정가능
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Product,ProductAdmin)