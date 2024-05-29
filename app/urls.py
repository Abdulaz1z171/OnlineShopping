from django.contrib import admin
from django.urls import path
from app.views import index_page,detail_product,add_product,add_comment,to_order

urlpatterns = [
    path('', index_page, name='index'),
    path('category/<int:cat_id>/', index_page, name='category_by_id'),
    path('detail/<int:pk>/',detail_product,name='detail'),
    path('add_product/',add_product,name = 'add_product'),
    path('detail<int:pk>/comment',add_comment,name = 'add_comment'),
    path('detail<int:pk>/order',to_order,name = 'to_order')
 ]
