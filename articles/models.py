from django.db import models
from django.shortcuts import reverse
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Article(models.Model):
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="uploads/%Y/%m/%d", blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        if len(self.text) >= 51:
            return self.text[:50]
        return self.text

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})
