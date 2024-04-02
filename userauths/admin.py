from django.contrib import admin
from userauths.models import user
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=['username', 'email', 'bio']

admin.site.register(user, UserAdmin)