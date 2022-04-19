from random import choice
import string
from hashids import Hashids

def generate_short_id(url: str, num_of_chars: int) -> str:
    """Function to generate short_id of specified number of characters"""
    hashids = Hashids(salt="I prefer sweet @w@", min_length=6)
    return ''.join(choice(string.ascii_letters+string.digits) for _ in range(num_of_chars))
    #print("!!!! "+ hashids.encode(url) + "<<<<<")
    #return hashids.encode(url) 
