from django.db import models
from .validators import validate_file_extension

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add = True)
    banner = models.FileField(default = 'fallback.png', blank = True, validators=[validate_file_extension]) # Image

    def __str__(self):
        return self.title