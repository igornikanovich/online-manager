# Generated by Django 2.2.6 on 2019-10-31 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='data',
            field=models.DateTimeField(auto_now=True),
        ),
    ]