from django.contrib import admin
from .models import Movie, Actor
from django.contrib.auth.models import User, Group


admin.site.register(Movie)
admin.site.register(Actor)

admin.site.unregister(User)
admin.site.unregister(Group)
