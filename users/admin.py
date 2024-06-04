from django.contrib import admin
from .models import User, Code


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'user_roll', 'user_type', 'user_status', 'gender')
    list_filter = ('user_roll', 'user_type', 'user_status', 'gender')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)


@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'is_confirm', 'user', 'time', 'user_roll')
    list_filter = ('is_confirm', 'time', 'user_roll')
    search_fields = ('code', 'user__username')
    ordering = ('-time',)
