# Generated by Django 4.0.1 on 2022-01-20 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, null=True)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=50, null=True)),
                ('profile_image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pic')),
                ('bio', models.TextField(null=True)),
                ('profiletype', models.CharField(blank=True, choices=[("Bff's", "Bff's"), ('Dating', 'Dating'), ('Business', 'Business')], default=None, max_length=50, null=True)),
                ('blocked_by', models.ManyToManyField(blank=True, related_name='blocked', to=settings.AUTH_USER_MODEL)),
                ('likeability', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
