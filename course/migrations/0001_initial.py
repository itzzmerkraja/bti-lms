# Generated by Django 4.2.5 on 2023-09-08 07:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userauth', '0004_alter_userdetail_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('pic', models.ImageField(upload_to='coursepics')),
                ('cr_hours', models.IntegerField(default=0)),
                ('batch', models.ManyToManyField(to='userauth.batch')),
                ('teacher', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
