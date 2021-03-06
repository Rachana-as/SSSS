from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Profile(models.Model):
    GENDER_C = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other")
    ]
    PROFILE_T = [
        ("Bff's", "Bff's"),
        ("Dating", "Dating"),
        ("Business", "Business")
    ]
    

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=50, blank=True, null=True, choices=GENDER_C)
    profile_image = models.ImageField(upload_to='profile_pic', default="default.jpg", null=True, blank=True)
    bio = models.TextField(null=True)
    profiletype = models.CharField(max_length=50, choices=PROFILE_T, default=None, null=True, blank=True)
    likeability = models.ManyToManyField( User, related_name="likes", blank=True)
    blocked_by = models.ManyToManyField(User, related_name="blocked", blank=True)

    def __str__(self):
        return f"{self.full_name} Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_image.path)

        if img.height > 200 or img.width > 200:
            output_size = (250, 250)
            img.thumbnail(output_size)
            img.save(self.profile_image.path)

    @property
    def num_likes(self):
        return self.likeability.all().count()
