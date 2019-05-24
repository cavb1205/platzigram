from django.contrib import admin

from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """post admin"""

    list_display = ('id',
        'title',
        'user',
        'photo',
        'created',
        'modified')