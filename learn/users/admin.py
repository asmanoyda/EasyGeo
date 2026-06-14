from django.contrib import admin

from users.models import User




@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # This makes the field read-only during both creation and editing
    readonly_fields = ('joined',)