from django.contrib import admin
from .models import gallery,images,event,Registration

# Register your models here.
admin.site.register(gallery)
admin.site.register(images)
admin.site.register(event)
admin.site.register(Registration)