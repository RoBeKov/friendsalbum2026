from django.core.exceptions import ValidationError


def validate_size(value):
    if value.size > 5 * 1024 * 1024:
        raise ValidationError("Picture is more than 5 megabytes!")