from django.contrib import admin

from port_scanner_app.models import Result,Request

# Register your models here.
admin.site.register(Result)
admin.site.register(Request)