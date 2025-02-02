from django.db import models
from accounts.models import CustomUser


class ProcessedImage(models.Model):
    user = models.ForeignKey(CustomUser, null=True,
                             blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    image_url = models.URLField(max_length=200, null=True, blank=True)
    result = models.CharField(max_length=100, null=True, blank=True)
    confidence_score = models.FloatField(null=True, blank=True)
    processed_at = models.DateTimeField(auto_now_add=True)


# ========== info ================
class MainTitle(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class SubTitle(models.Model):
    main_title = models.ForeignKey(
        MainTitle, on_delete=models.CASCADE, related_name="subtitles")
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
