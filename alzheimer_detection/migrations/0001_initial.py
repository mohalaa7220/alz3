# Generated by Django 5.0.2 on 2025-01-30 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('image_url', models.URLField(blank=True, null=True)),
                ('result', models.CharField(blank=True, max_length=100, null=True)),
                ('confidence_score', models.FloatField(blank=True, null=True)),
                ('processed_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
