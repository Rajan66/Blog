# Generated by Django 4.2.1 on 2023-05-30 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='A Beautiful Blog', max_length=255),
        ),
    ]
