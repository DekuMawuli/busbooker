from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm

admin.site.title = "Bus Booker"


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (
            'Personal info', {'fields': ('first_name', 'last_name', 'email', 'role', 'phone')}
        ),
        (
            'Permissions', {
                'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
            }
        ),
        (
            'Important dates', {'fields': ('last_login', 'date_joined')}
         ),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', "role", "phone", 'password1', 'password2'),
        }),
    )
