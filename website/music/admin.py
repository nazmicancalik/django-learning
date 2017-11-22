from django.contrib import admin
from .models import Album, Song

# Register album in admin page
admin.site.register(Album)
admin.site.register(Song)

