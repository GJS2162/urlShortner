# Generated by Django 4.1.5 on 2023-05-12 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userurls',
            name='urls',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
