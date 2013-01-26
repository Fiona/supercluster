# Django imports
from django.contrib import admin

# Project imports
from .models import Game


class GameAdmin(admin.ModelAdmin):
    pass
admin.site.register(Game, GameAdmin)
