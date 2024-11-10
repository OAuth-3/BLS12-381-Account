from .module import SigningKey, SECP256k1
from util import hash
from binascii import unhexlify, hexlify
import hashlib
from util.ripemd160 import RIPEMD160

# ! create keypair from seed
def keypair_gen_seed(seed: bytes) -> (str, str, str, str):
    # $ 1. create private key
    private_key_bytes = hashlib.sha256(seed).digest()
    private_key = SigningKey.from_string(private_key_bytes, curve=SECP256k1).to_string().hex()

    # $ 2. convert wif private key
    wif_private_key = convert_to_wif_private_key(private_key_bytes)

    # $ 3. create public key
    public_key = SigningKey.from_string(private_key_bytes, curve=SECP256k1).get_verifying_key().to_string().hex()

    # $ 4. convert bitcoin address
    bitcoin_address = convert_to_bitcoin_address(unhexlify(public_key))

    # $ 5. return the keys and address
    return private_key, wif_private_key, public_key, bitcoin_address

# ! create keypair from private key
def keypair_gen_privatekey(is_wif_private_key: bool, encoded_key: str) -> (str, str, str, str):
    # $ 1. decode the private key
    private_key_bytes = hash.base58_decode(encoded_key)[1:-4] if is_wif_private_key else bytes.fromhex(encoded_key)
    private_key = SigningKey.from_string(private_key_bytes, curve=SECP256k1).to_string().hex()

    # $ 2. create wif private key
    wif_private_key = convert_to_wif_private_key(private_key_bytes)

    # $ 3. create public key
    public_key = SigningKey.from_string(private_key_bytes, curve=SECP256k1).get_verifying_key().to_string().hex()

    # $ 4. convert bitcoin address
    bitcoin_address = convert_to_bitcoin_address(unhexlify(public_key))

    # $ 5. return the keys and address
    return private_key, wif_private_key, public_key, bitcoin_address

# ! convert private key to wif
def convert_to_wif_private_key(private_key_bytes: bytes) -> str:
    extended_key = b'\x80' + private_key_bytes
    checksum = hashlib.sha256(hashlib.sha256(extended_key).digest()).digest()[:4]
    wif_private_key = hash.base58_encode(extended_key + checksum)
    
    return wif_private_key

# ! convert public key to bitcoin address
def convert_to_bitcoin_address(public_key_bytes: bytes) -> str:
    sha256 = hashlib.sha256(b'\x04' + public_key_bytes).digest()
    ripemd160_hash = RIPEMD160()
    ripemd160_hash.update(sha256)
    public_key_hash = ripemd160_hash.digest()
    
    public_key_hash_with_network = b'\x00' + public_key_hash
    checksum = hashlib.sha256(hashlib.sha256(public_key_hash_with_network).digest()).digest()[:4]
    binary_address = public_key_hash_with_network + checksum
    bitcoin_address = hash.base58_encode(binary_address)
    
    return bitcoin_address