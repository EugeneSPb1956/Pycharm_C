from django.contrib import admin
from .models import Artists, Albums, Studio, Tracks

# Register your models here.

@admin.register(Artists)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city', 'year1', 'active')
    search_fields = ('name', 'country')
    # search_fields = ('name__contains', 'country')
    # search_fields = ('name__icontains', 'country')  # i - без учетв регистра

@admin.register(Albums)
class AlbumsAdmin(admin.ModelAdmin):
    pass

@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    pass

@admin.register(Tracks)
class TracksAdmin(admin.ModelAdmin):
    pass
