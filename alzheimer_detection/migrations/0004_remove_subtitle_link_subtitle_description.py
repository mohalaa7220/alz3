# Generated by Django 5.0.2 on 2025-02-02 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alzheimer_detection', '0003_maintitle_subtitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtitle',
            name='link',
        ),
        migrations.AddField(
            model_name='subtitle',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
