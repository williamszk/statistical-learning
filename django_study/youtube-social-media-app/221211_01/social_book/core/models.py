from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField() 
    bio = models.TextField(blank=True)
    profile_img = models.ImageField(upload_to="profile_images", default="blank-profile-picture.jpeg") 
    location = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return self.user.username





