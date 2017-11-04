from django.db import models
from django.contrib.auth.models import User


class Level(models.Model):
    """ Model for a level of the game """
    users = models.ManyToManyField(User, through='user_level')

    def get_stages(self):
        """ Returns the stages for a specific level """
        return self.stage_set.objects.all()

    def __str__(self):
        return "Level {}".format(self.id)


class Stage(models.Model):
    """ Model for a stage of a level """
    users = models.ManyToManyField(User, through='user_stage')
    # a stage has 1 level
    level = models.ForeignKey(Level)

    def get_stage_url(self):
        return "stage_{}.html".format(self.id)

    def __str__(self):
        """
        String representation for a stage. Intended for admin site.
        """
        return "{}: Stage {}".format(self.level, self.id)


class UserLevel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)


class UserStage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)