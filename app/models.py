from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Recent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=True, blank=False, null=False)

    def __str__(self) -> str:
        return self.user.username
