from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from api.models import *

# Register your models here.

class UsersAdmin(BaseUserAdmin):
    list_display = ['id', "username", "is_interviewer"]

admin.site.register(CustomUser, UsersAdmin)
admin.site.register(TimeSlot)