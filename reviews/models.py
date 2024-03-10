from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Review(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "reviews")

    title = models.CharField(max_length = 63)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return f"Review {self.title} by {self.author.username} - {self.pub_date}"
    
    class Meta:
        ordering = ["pub_date"]
        verbose_name = "Review"
        verbose_name_plural = "Reviews"