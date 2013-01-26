# Django imports
from django.conf.urls import patterns, include, url
from django.contrib import admin

# Project imports
from .utils import check_and_advance_all_game_turns

# This checks the turn timer on all games and advances them
# to the next turn if necessary. It uses threading to check
# every minute.
check_and_advance_all_game_turns()

# Empty url patterns
urlpatterns = patterns('')
