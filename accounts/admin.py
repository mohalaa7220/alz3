from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ['first_name', 'last_name',
                    'email', 'phone_number', 'age', 'gender', 'education_level']
    search_fields = ['username', 'email']


admin.site.register(CustomUser, CustomUserAdmin)
