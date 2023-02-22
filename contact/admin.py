from django.contrib import admin
from .models import ContactModel, ContactLink, About, Social, ImageAbout


class ImageAboutInline(admin.StackedInline):
    model = ImageAbout
    extra = 1


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'create_at']
    list_display_links = ('name',)


@admin.register(About)
class About(admin.ModelAdmin):
    list_display = ['id', 'name', 'mini_text']
    inlines = [ImageAboutInline]
    save_on_top = True
    save_as = True


admin.site.register(ContactLink)
admin.site.register( ImageAbout)
admin.site.register(Social)


