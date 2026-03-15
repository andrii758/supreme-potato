from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to="avatars/", default="static/img/default_avatar.jpg"
    )
    banner = models.ImageField(
        upload_to="banners/", default="static/img/default_banner.jpg"
    )
    bio = models.TextField(max_length=160, blank=True)
    location = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)

    # subscription system
    following = models.ManyToManyField(
        "self",
        through="Follow",
        related_name="followers",
        symmetrical=False,
    )
    
    USERNAME_FIELD = 'username'

    def __str__(self):
        return f"@{self.user.username} Profile"


class Follow(models.Model):
    user_from = models.ForeignKey(
        Profile, related_name="rel_from_set", on_delete=models.CASCADE
    )
    user_to = models.ForeignKey(
        Profile, related_name="rel_to_set", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

