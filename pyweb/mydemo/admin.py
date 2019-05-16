from django.contrib import admin

# Register your models here.
from mydemo.models import User


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ["id","username"]
    search_fields = ["id","username"]
    list_per_page = 3


admin.site.register(User,UserInfoAdmin)
