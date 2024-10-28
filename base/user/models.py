from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)

    auto_answer = models.BooleanField(null=False, blank=False, default=False)
    time_auto_answer = models.TimeField(default="00:05:00")

    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)

    def __str__(self):
        """
        Returns a string representation of the contact.

        Returns a string of the format 'first_name_last_name'.

        Returns:
        str: A string representation of the contact.
        """
        return f'{self.first_name}_{self.last_name}'

