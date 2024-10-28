
import hashlib
from .module import SigningKey, SECP256k1

def create_private_key_from_seed(seed: bytes):
    return hashlib.sha256(seed).digest()

def generate_key_pair(seed: bytes):
    private_key_bytes = create_private_key_from_seed(seed)
    private_key = SigningKey.from_string(private_key_bytes, curve=SECP256k1)
    public_key = private_key.get_verifying_key()
    return private_key, public_key

def export_keys(private_key, public_key):
    private_key_hex = private_key.to_string().hex()
    public_key_hex = public_key.to_string().hex()
    return private_key_hex, public_key_hex