from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^register/$',views.register),
    url(r'^login/$',views.login),
    url(r'center_info/$',views.center_info),
    url(r'center_order/$',views.center_order),
    url(r'center_site/$',views.center_siter),
]