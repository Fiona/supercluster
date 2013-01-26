from datetime import datetime
from django.db import models


class Game(models.Model):
    """
    Each game currently running    
    """
    galaxy_name = models.CharField(max_length = 255)
    num_stars = models.IntegerField(default = 50)
    num_players = models.IntegerField(default = 0)
    turn = models.IntegerField(default = 0)
    turn_length = models.IntegerField(default = 60)
    last_turn_time = models.DateTimeField(blank = True, null = True, auto_now_add = True)
    

    def advance_to_next_turn(self):
        """
        Ends the current turn, runs all the pending player actions and
        advances to the next turn.
        """
        self.turn += 1
        self.last_turn_time = datetime.now()
        self.save()
        

    def is_turn_over(self):
        """
        Returns a bool indicating if the current turn is over and should
        end.
        """
        if (datetime.now() - self.last_turn_time).minutes >= self.turn_length:
            return True
        return False


    def check_and_advance_turn(self):
        """
        Checks if the current turn is over and advances it if so.
        """
        if self.is_turn_over():
            self.advance_to_next_turn()
