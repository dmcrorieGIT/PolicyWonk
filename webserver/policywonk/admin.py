# todo/admin.py

from django.contrib import admin
from .models import UserModel # add this

class UserModelAdmin(admin.ModelAdmin):  # add this
    list_display = ('name', 'last_name') # add this

# Register your models here.
admin.site.register(UserModel, UserModelAdmin) # add this