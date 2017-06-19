from django.conf.urls import url
import views

urlpatterns = [
            url(r'^$', views.index),
            url(r'^list(\d*)_(\d*)/$', views.goodslist),
            url(r'^detail(\d+)/$',views.goods_detail),

        ]