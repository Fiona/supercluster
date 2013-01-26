# Python imports
from threading import Timer

# Project imports
from .models import Game


def check_and_advance_all_game_turns():
    """
    This is intially run when the server comes up.
    It iterates and checks the turn status of all running games.
    It runs itself every minute using a thread.
    """
    for game in Game.objects.all():
        game.check_and_advance_turn()

    Timer(60, check_and_advance_all_game_turns).start()

