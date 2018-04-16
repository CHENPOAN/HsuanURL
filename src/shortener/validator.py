from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_url(value):
    url_validator = URLValidator()
    reg_val = value
    if "http" in reg_val:
        new_val = reg_val
    else:
        new_val = "http://" + reg_val

    try:
        url_validator(new_val)
    except:
        raise ValidationError("Invalid URL for this field")
    return new_val

def validate_dot_com(value):
    if not "com" in value:
        raise ValidationError("This is not valid because of no .com")
    return value