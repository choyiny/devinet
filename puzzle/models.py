from django.db import models
from django.contrib.auth.models import User


class Level(models.Model):
    """ Model for a level of the game """
    users = models.ManyToManyField(User, through='UserLevel')

    def get_stages(self):
        """ Returns the stages for a specific level """
        return self.stage_set.objects.all()

    def __str__(self):
        return "Level {}".format(self.id)


class Stage(models.Model):
    """ Model for a stage of a level """
    users = models.ManyToManyField(User, through='UserStage')
    # a stage has 1 level
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

    # stage has a hint
    hint = models.CharField(max_length=255, default="There is not hint for this level.");

    def get_stage_url(self):
        return "stage_{}.html".format(self.id)

    def get_level(self):
        """ Returns the level the stage is part of. """
        return self.level

    def __str__(self):
        """
        String representation for a stage. Intended for admin site.
        """
        return "{}: Stage {}".format(self.level, self.id)


class UserLevel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " -> Level " + str(self.level.id)


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coins = models.IntegerField(default=3)

    def __str__(self):
        return self.user.username + ": " + str(self.coins)

    def get_coins(self):
        return self.coins

    def add_coins(self, coin):
        self.coins += coin

    def remove_coins(self, coin):
        self.coins -= coin


class UserStage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " -> Stage " + str(self.stage.id)
