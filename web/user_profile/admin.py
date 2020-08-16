from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_image')
    # list_filter = ()
    search_fields = ('user',)  # по какому полю категории искать
    readonly_fields = ('get_image',)
    save_on_top = True  # save button on top

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} width='25' height='25'")

    get_image.short_description = 'Avatar'

