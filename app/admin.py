from __future__ import unicode_literals


from django.contrib import admin
from django.contrib.auth import admin as auth

from .models import UUIDUser, Forum, Respostas, Anime, Arts
admin.site.register(UUIDUser)
admin.site.register(Forum)
admin.site.register(Respostas)
admin.site.register(Anime)
admin.site.register(Arts)
