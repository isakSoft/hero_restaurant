from django.db import models
import datetime


class Restaurant(models.Model):
    """This class is defining restaurant model"""
    name = models.CharField(max_length=255, unique=True, blank=False)
    opens_at = models.TimeField(default=datetime.time(9, 00))
    closes_at = models.TimeField(default=datetime.time(22, 00))

    def __str__(self):
        """Humanized model representation"""
        return "{}".format(self.name)
