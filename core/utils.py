from random import choice
import string
import validators


def generate_short_id(url: str, num_of_chars: int) -> str:
    """Function to generate short_id of specified number of characters"""
    return ''.join(choice(string.ascii_letters+string.digits) for _ in range(num_of_chars))

def validate_url(url: str):
    status = validators.url(url)
    if status:
        return {}, 200
    return {"error": "invalid url"}, 400
