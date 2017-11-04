from django.db import models
from django.contrib.auth.models import User

class user_level(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

class user_stage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)

class Level(models.Model):
    """ Model for a level of the game """

    def get_stages(self):
        """ Returns the stages for a specific level """
        return self.stage_set.objects.all()

    def __str__(self):
        return "Level {}".format(self.id)


class Stage(models.Model):
    """ Model for a stage of a level """
    # a stage has 1 level
    level = models.ForeignKey(Level)

    # name of stage
    name = models.TextField()

    def __str__(self):
        return self.name
