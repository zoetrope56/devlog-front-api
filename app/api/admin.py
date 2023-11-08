from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Tag)
admin.site.register(models.File)
admin.site.register(models.Content)
admin.site.register(models.ContentsDetail)
# admin.site.register(models.ContentsTag)