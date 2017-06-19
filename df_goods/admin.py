from django.contrib import admin
from models import *

# Register your models here.


class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'ttitle','isDelete']
    list_per_page = 10
    actions_on_bottom = True

class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id','gtitle','gprice', 'gunit','gclick','gkucun','gtype','isDelete']
    list_per_page = 10
    actions_on_bottom = True
admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(GoodsInfo,GoodsInfoAdmin)