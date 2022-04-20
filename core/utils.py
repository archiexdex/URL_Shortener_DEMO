from random import choice
import string

def generate_short_id(url: str, num_of_chars: int) -> str:
    """Function to generate short_id of specified number of characters"""
    return ''.join(choice(string.ascii_letters+string.digits) for _ in range(num_of_chars))
