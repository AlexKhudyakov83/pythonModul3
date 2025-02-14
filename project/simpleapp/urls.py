from django.urls import path
# Импортируем созданные нами представления
from .views import ProductsList, ProductDetail, \
   ProductCreate, ProductUpdate, ProductDelete, subscriptions

urlpatterns = [

   path('', ProductsList.as_view(), name='product_list'),
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>', ProductDetail.as_view(), name='product_detail'),
   path('create/', ProductCreate.as_view(), name='product_create'),
   path('<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
   path('<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
   path('subscriptions/', subscriptions, name='subscriptions'),

]