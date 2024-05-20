from django.contrib import admin
from . import models

admin.site.register(models.BagModel)
admin.site.register(models.LabelModel)
admin.site.register(models.ImageOfBagModel)
admin.site.register(models.CategoryModel)
