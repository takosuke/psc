from django.db import models
from django.utils import timezone
import datetime
from easy_thumbnails.fields import ThumbnailerImageField
from taggit.managers import TaggableManager
from taggit.models import Tag

class Post(models.Model):
    title = models.CharField(max_length = 200)
    date = models.DateTimeField()
    text = models.TextField(blank=True)
    url = models.URLField(blank=True)
    def tag_helptext():
        help_text = "Options: "
        for t in Tag.objects.all():
            help_text += t.name + " ||| "
        return help_text
    tags = TaggableManager(blank=True, help_text = tag_helptext())
    image  = ThumbnailerImageField(upload_to = 'cover', blank=True)
    def __unicode__(self):
        return self.title
    def title_contains_penis(self):
        return "penis" in self.title
    def was_published_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)
        

