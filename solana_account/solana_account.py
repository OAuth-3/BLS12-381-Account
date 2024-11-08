from .module.ed25519_oop import SigningKey, VerifyingKey
from util import hash

# ! create keypair from seed
def keypair_gen_seed(seed: bytes) -> (str, str, str):
    # $ 1. create private key
    private_key = hash.base58_encode(SigningKey(seed).to_bytes())

    # $ 2. create public key
    public_key = SigningKey(seed).get_verifying_key().to_bytes().hex()

    # $ 3. convert solana address
    solana_address = convert_to_solana_address(bytes.fromhex(public_key))

    # $ 4. return the keys and address
    return private_key, public_key, solana_address

# ! create keypair from private key
def keypair_gen_privatekey(encoded_key: str) -> (str, str, str):
    # $ 1. decode the private key
    private_key_bytes = hash.base58_decode(encoded_key)
    private_key = hash.base58_encode(SigningKey(private_key_bytes).to_bytes())

    # $ 2. create public key
    public_key = SigningKey(private_key_bytes).get_verifying_key().to_bytes().hex()

    # $ 3. convert solana address
    solana_address = convert_to_solana_address(bytes.fromhex(public_key))

    # $ 4. return the keys and address
    return private_key, public_key, solana_address

# ! convert public key to solana address
def convert_to_solana_address(public_key_bytes: bytes) -> str:
    solana_address = hash.base58_encode(public_key_bytes)

    return solana_address