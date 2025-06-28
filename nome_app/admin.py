from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import post

# Register your models here.
class postAdmin(admin.ModelAdmin):
  list_display = ("title", "author")

# Register your models here.
admin.site.register(post)