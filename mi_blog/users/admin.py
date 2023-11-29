from django.contrib import admin
from django.contrib.auth.models import Group, User
from .forms import Profile

class ProfileInLine(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields =["username"]
    inlines = [ProfileInLine]

admin.site.register(Profile)
# Register your models here.
