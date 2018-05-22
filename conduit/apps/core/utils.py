import random
import string

def generate_random_string(chars=string.ascii_lowercase + string.digits, size=6):
    return ''.join(random.choice(chars) for _ in range(size))