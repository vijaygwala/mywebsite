# Generated by Django 3.0.5 on 2020-10-17 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_profile_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to=settings.AUTH_USER_MODEL),
        ),
    ]
