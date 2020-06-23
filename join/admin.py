from django.contrib import admin
from .models import Join,Subcriber,Address
# Register your models here.

class JoinAdmin(admin.ModelAdmin):
    list_display=['email','first_name','timestamp']

admin.site.register(Join,JoinAdmin)
admin.site.register(Subcriber)
admin.site.register(Address)
