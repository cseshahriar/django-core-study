from django.core.exceptions import ValidationError

# custom validation
def validate_author_email(value):
    if not "@" in value:
        raise ValidationError("Invalid email address!")
    return value;
