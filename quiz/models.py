from django.db import models


class MainTitle(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title


class Question(models.Model):
    main_title = models.ForeignKey(
        MainTitle, on_delete=models.CASCADE, related_name="questions")
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.text
