# Generated by Django 5.0 on 2024-01-10 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]
