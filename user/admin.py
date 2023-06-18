from django.contrib import admin

from user.models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['image_tag','user_name', 'phone']

    list_display_links = ['image_tag','user_name', 'phone']

