from django.db import models

# Create your models here.
class ContactMessage(models.Model):

    """Model representing a contact message."""

    name = models.CharField(max_length=32)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name + ', ' + self.message[:10]
