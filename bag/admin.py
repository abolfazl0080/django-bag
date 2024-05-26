from django.contrib import admin
from . import models


class ImageOfBagInline(admin.TabularInline):
    model = models.ImageOfBagModel


class BagAdmin(admin.ModelAdmin):
    inlines = [
        ImageOfBagInline
    ]

admin.site.register(models.BagModel, BagAdmin)
admin.site.register(models.LabelModel)
admin.site.register(models.ImageOfBagModel)
admin.site.register(models.CategoryModel)
