from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Tags)
admin.site.register(models.File)
admin.site.register(models.Contents)
admin.site.register(models.ContentsDetail)
admin.site.register(models.ContentsTags)