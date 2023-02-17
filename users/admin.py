from django.contrib import admin
from . import forms
from . import models
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = models.CustomUser
    add_form = forms.CustomUserCreationForm
    form = forms.CustomUserChangeForm
    list_display = ["username", "age", "email", "is_staff"] #what fields of the user to be displayed in the admin panel


admin.site.register(models.CustomUser, CustomUserAdmin)