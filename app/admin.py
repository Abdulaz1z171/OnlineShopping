from django.contrib import admin
from django.contrib.auth.models import User,Group
from .models import Product,Comment,Category,Order





# admin.site.register(Product)
# admin.site.register(Comment)
# admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','image','rating','discount','is_expensive']
    list_filter = ['created_at','price','category']

    def is_expensive(self,obj):
        return obj.price > 300
    is_expensive.boolean = True




@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['username','email','created_at']
    list_filter = ['created_at']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer','phone_number','product']



admin.site.unregister(User)
admin.site.unregister(Group)