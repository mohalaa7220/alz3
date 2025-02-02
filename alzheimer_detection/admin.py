from django.contrib import admin
from .models import (ProcessedImage, MainTitle, SubTitle)


class CustomProcessedImage(admin.ModelAdmin):
    model = ProcessedImage
    list_display = ['user_email', 'image_url',
                    'result', 'confidence_score', 'processed_at']

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'User Email'


admin.site.register(ProcessedImage, CustomProcessedImage)
admin.site.register(MainTitle)
admin.site.register(SubTitle)
