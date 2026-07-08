from django.db import models

class Video(models.Model):
    video = models.FileField(upload_to='gallery/videos/')
    is_cover = models.BooleanField(default=False)


