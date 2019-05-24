from django.contrib import admin

from users.models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """profile admin"""

    list_display = ('id', 'user', 'website', 'phone_number','picture')
    list_display_links = ('user', 'website')

    search_fields = ('user__username', 'user__email')

    list_filter = ('user__is_active', 'created')