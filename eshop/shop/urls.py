from django.urls import path

from . import views as v

urlpatterns = [
    path('', v.startpage, name='base'),
    path('product.html', v.product, name='product'),
    path('product/<str:name>', v.product, name='product'),
    path('tool1.html', v.product, name='index.html')
]