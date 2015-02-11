from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

class Album(models.Model):
    artist = models.CharField(max_length=100)

class Track(models.Model):
    album = models.ForeignKey(Album)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    def __unicode__(self):
        return '%d: %s' % (self.order, self.title)