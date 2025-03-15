from django.urls import path
from .views import home_page,Waters_list,Waater_add,Product_detail,Product_delete,Product_update

urlpatterns = [
    path('', home_page, name='home'),
    path('list/', Waters_list.as_view(), name='list'),
    path('add_product/',Waater_add.as_view(),name="add-product"),
    path('detail/<int:pk>',Product_detail.as_view(),name="detail"),
    path('delete/<int:pk>',Product_delete.as_view(),name="product-delete"),
    path('update/<int:pk>',Product_update.as_view(),name="product-update"),
    
]

