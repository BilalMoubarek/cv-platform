from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'phone_number', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active', 'date_joined']
    search_fields = ['email', 'first_name', 'last_name']
    readonly_fields = ['last_login', 'date_joined']
    ordering = ['email']
    
    fieldsets = (
        ('🔐 معلومات الدخول', {
            'fields': ('email', 'password')
        }),
        ('👤 المعلومات الشخصية', {
            'fields': ('first_name', 'last_name', 'phone_number', 'birth_date')
        }),
        ('🔑 الصلاحيات', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('📅 التواريخ', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    
    add_fieldsets = (
        ('🔐 إنشاء مستخدم جديد', {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)