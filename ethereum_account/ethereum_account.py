from .module import SigningKey, SECP256k1
from util import hash
import hashlib

# ! create keypair from seed
def keypair_gen_seed(seed: bytes):
    # $ 1. create private key
    private_key_bytes = hashlib.sha256(seed).digest()
    private_key = SigningKey.from_string(private_key_bytes, curve=SECP256k1).to_string().hex()

    # $ 2. create public key
    public_key = SigningKey.from_string(private_key_bytes, curve=SECP256k1).get_verifying_key().to_string().hex()

    # $ 3. convert ethereum address
    ethereum_address = convert_to_ethereum_address(bytes.fromhex(public_key))

    # $ 4. return the keys and address
    return private_key, public_key, ethereum_address

# ! create keypair from private key
def keypair_gen_privatekey(encoded_key: str):
    # $ 1. decode the private key
    private_key_bytes = bytes.fromhex(encoded_key)
    private_key = SigningKey.from_string(private_key_bytes, curve=SECP256k1).to_string().hex()

    # $ 2. create public key
    public_key = SigningKey.from_string(private_key_bytes, curve=SECP256k1).get_verifying_key().to_string().hex()

    # $ 3. convert ethereum address
    ethereum_address = convert_to_ethereum_address(bytes.fromhex(public_key))

    # $ 4. return the keys and address
    return private_key, public_key, ethereum_address

# ! convert public key to ethereum address
def convert_to_ethereum_address(public_key_bytes: bytes):
    keccak256 = hash.Keccak256()
    keccak256.update(public_key_bytes)
    public_key_hash = keccak256.digest()
    ethereum_address = "0x" + public_key_hash[-20:].hex()

    return ethereum_address