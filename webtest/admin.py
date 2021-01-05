from django.contrib import admin
from webtest.models import Webcase,Webcasestep
# Register your models here.


class WebcaseAdmin(admin.TabularInline):
    list_display = ['webcasename', 'webtestresult','create_time','id','product']
    model = Webcase
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc','create_time','id']
    inlines = [WebcaseAdmin]


class WebcasestepAdmin(admin.TabularInline):
    list_display=['webcasename','webteststep','webtestobjname','webfindmethod','webevelement','weboptmethod','webassertdata','webtestresult','create_time','id','webcase']
    model = Webcasestep
    extra=1

class WebcaseAdmin(admin.ModelAdmin):
    list_display = ['webcasename', 'webtestresult','create_time','id']
    inlines = [WebcasestepAdmin]

admin.site.register(Webcase,WebcaseAdmin)