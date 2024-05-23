from django.db import models
from django.contrib.auth.models import User


def get_default_user():
    return User.objects.get_or_create(username='admin')[0]

# Create your models here.
class Participant(models.Model):
    """Model representing a participant"""
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        """String for representing the Model object."""
        return self.last_name + ", " + self.first_name