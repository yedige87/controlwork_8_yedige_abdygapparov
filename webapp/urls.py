from django.urls import path

from webapp.views.base import IndexView
from webapp.views.products import ProductDetail, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns =[
    path("", IndexView.as_view(), name='index'),
    path("product/<int:pk>", ProductDetail.as_view(), name='product_detail'),
    path('product/add/', ProductCreateView.as_view(), name='product_add'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/confirm_delete/', ProductDeleteView.as_view(), name='confirm_delete'),
]