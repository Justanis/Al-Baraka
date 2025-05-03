import random

def generate_confirmation_code(length=6):
    """Generate a random numeric confirmation code."""
    return ''.join(str(random.randint(0, 9)) for _ in range(length))
