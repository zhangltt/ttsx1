from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^register/$',views.register),
    url(r'^login/$',views.login),
    url(r'^login_handler/$',views.login_handler),
    url(r'^logout/$', views.logout),
    url(r'^center_info/$',views.center_info),
    url(r'^info_handler/$', views.info_handler),
    url(r'^center_order/$',views.center_order),
    url(r'^center_site/$',views.center_siter),
    url(r'^site/$', views.siter_handler),
]