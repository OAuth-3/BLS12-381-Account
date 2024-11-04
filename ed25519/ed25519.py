from .module.ed25519_oop import SigningKey, VerifyingKey

def keypair_gen_seed(seed: bytes):
    private_key = SigningKey(seed)
    public_key = private_key.get_verifying_key()
    return private_key, public_key

def export_keys(private_key, public_key):
    private_key_hex = private_key.to_ascii(encoding="hex").decode('utf-8')
    public_key_hex = public_key.to_ascii(encoding="hex").decode('utf-8')
    return private_key_hex, public_key_hex