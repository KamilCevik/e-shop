from django.contrib import admin

from home.models import Setting, ContactFormMessage

# Register your models here.

admin.site.register(Setting)


@admin.register(ContactFormMessage)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'note', 'status']
    list_filter = ['status']
    list_display_links = ['name', 'email', 'subject', 'message', 'note']
