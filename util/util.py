import secrets

def create_random(count: int):
    return secrets.token_bytes(count)
