from django.contrib import admin

# Register your models here.

from .models import MessageType, Message

admin.site.register(MessageType)
admin.site.register(Message)
