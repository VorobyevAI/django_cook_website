from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin


class RecipeInLine(admin.StackedInline):
    model = models.Recipe
    extra = 1


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'create_at', 'id']
    inlines = [RecipeInLine]
    save_on_top = True
    save_as = True


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'prep_time', 'cook_time', 'id']


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Comment)