from imagekit.admin import AdminThumbnail
from django.contrib import admin
from Boroughs.models import Borough, Photo

class BoroughsAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    list_display = ('title', 'slug', 'author',
                    'created', 'modified')
    admin_thumbnail = AdminThumbnail(image_field='main_img')
    list_filter = ['title', 'created', 'author']
    search_fields = ['title', 'author']


admin.site.register(Borough, BoroughsAdmin)


class PhotoAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None,               {'fields': ['borough']}),
    #     # ('Date information', {'fields': ['created'], 'classes': ['collapse']}),
    # ]

    list_display = ('content', 'image', 'borough', 'approved', 'was_published_recently', 
                    'first_name', 'last_name', 'email', 'created')
    list_filter = ['borough', 'created', 'email']
    search_fields = ['borough', 'content']

admin.site.register(Photo, PhotoAdmin)
