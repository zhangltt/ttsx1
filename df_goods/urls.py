from django.conf.urls import url
import views

urlpatterns = [
            url(r'^$', views.index),
            url(r'^list(\d*)_(\d*)/$', views.goodslist),
            url(r'^goods_order/$',views.goods_order),

        ]