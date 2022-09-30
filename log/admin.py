from django.contrib import admin
from .models import CustomUser, UserRole
# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','mobile_number','role','is_admin','is_active','is_staff']
    search_fields = ['id','first_name']

@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ['id','name']