from django.db import models

class Post(models.Model):
      title = models.CharField(max_length = 100)
      datetime = models.DateTimeField('date published')
      content = models.TextField(max_length=5000)

      def __unicode__(self):
           return self.title 
