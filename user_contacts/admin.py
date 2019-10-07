from django.contrib import admin

from .models import UserContact


class UserContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'listing',
        'email',
        'contact_date'
    )
    list_display_links = (
        'id',
        'name'
    )
    search_fields = (
        'name',
        'email',
        'listing'
    )
    list_per_page = 25

admin.site.register(UserContact, UserContactAdmin)