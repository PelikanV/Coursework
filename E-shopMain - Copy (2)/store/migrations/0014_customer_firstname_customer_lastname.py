# Generated by Django 4.1.2 on 2022-11-10 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='firstname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='lastname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]