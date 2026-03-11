from django.core.validators import MinLengthValidator
from django.db import models

from friendsalbum2026.photo.validators import validate_size


# Create your models here.
class Photo(models.Model):
    photo = models.ImageField(
        validators=[
            validate_size
        ]
    )

    description = models.TextField(
        max_length=250,
        validators=(
            MinLengthValidator(10),
        ),
        blank=True,
        null=True,
    )

    author = models.TextField(
        max_length=150,
        validators=(
            MinLengthValidator(10),
        )
    )

    location = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    date_of_publication = models.DateField(
        auto_now=True,
    )