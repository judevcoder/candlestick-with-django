from django.conf.urls import url, include
from django.contrib import admin
import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^stock_data', views.stockdata, name='stockdata'),
]
