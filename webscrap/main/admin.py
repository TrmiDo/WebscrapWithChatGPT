from django.contrib import admin

# Register your models here.
from .models import WebContent,Detail
admin.site.register(WebContent)
admin.site.register(Detail)