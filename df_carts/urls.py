from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$',views.cart),
    url(r'^cart_handle/$',views.cart_handle),
    #url(r'^delete/$', views.delete),
    #url(r'^place/$',views.place),
]