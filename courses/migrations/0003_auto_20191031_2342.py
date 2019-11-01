# Generated by Django 2.2.6 on 2019-10-31 23:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_comment_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, limit_choices_to={'user_type': '2'}, related_name='students', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='teachers',
            field=models.ManyToManyField(blank=True, limit_choices_to={'user_type': '1'}, related_name='teachers', to=settings.AUTH_USER_MODEL),
        ),
    ]
