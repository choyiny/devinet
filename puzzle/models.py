from django.db import models


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

    def get_stage_url(self):
        return "stage_{}.html".format(self.id)

    def __str__(self):
        """
        String representation for a stage. Intended for admin site.
        """
        return "{}: Stage {}".format(self.level, self.id)
