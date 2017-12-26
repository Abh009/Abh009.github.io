from django.db import models

# Create your models here.

class Article(models.Model):
    headline = models.CharField(max_length = 100,null = False)
    content = models.CharField(max_length = 1000,null = False)
    author = models.CharField(max_length = 100, null = False)
    is_published = models.BooleanField(default = True)
    date_of_publication = models.DateTimeField(null = False)

    def __str__(self):
        return str(self.headline) + " - " + str(self.author)
