from util import util
from bls import bls, utils
from ecdsa import ecdsa
from ed25519 import ed25519

# * [COMMON] Generate multiple private and public key pairs
seed1: bytes = util.create_random(32)
seed2: bytes = util.create_random(32)

# % [BLS] Generate bls private keys and public keys
bls_sk1, bls_pk1 = bls.keypair_gen_seed(seed1)
bls_sk2, bls_pk2 = bls.keypair_gen_seed(seed2)

# % [BLS] [DISPLAY] Export keys for display purposes
print('[BLS] [SEED] Private Key 1:', utils.export_sk(bls_sk1))
print('[BLS] [SEED] Public Key 1:', utils.export_pk(bls_pk1))
print('[BLS] [SEED] Private Key 2:', utils.export_sk(bls_sk2))
print('[BLS] [SEED] Public Key 2:', utils.export_pk(bls_pk2))

# % [BLS] Import the private keys
bls_sk1_from_priv, bls_pk1_from_priv = bls.keypair_gen_privatekey(utils.export_sk(bls_sk1))
bls_sk2_from_priv, bls_pk2_from_priv = bls.keypair_gen_privatekey(utils.export_sk(bls_sk2))

# % [BLS] [DISPLAY] Export keys for display purposes
print('[BLS] [PRIVATE KEY] Private Key 1:', utils.export_sk(bls_sk1_from_priv))
print('[BLS] [PRIVATE KEY] Public Key 1:', utils.export_pk(bls_pk1_from_priv))
print('[BLS] [PRIVATE KEY] Private Key 2:', utils.export_sk(bls_sk2_from_priv))
print('[BLS] [PRIVATE KEY] Public Key 2:', utils.export_pk(bls_pk2_from_priv))

# ! [ECDSA] Generate ecdsa private keys and public keys
ecdsa_sk1, ecdsa_pk1 = ecdsa.keypair_gen_seed(seed1)
ecdsa_sk2, ecdsa_pk2 = ecdsa.keypair_gen_seed(seed2)

# ! [ECDSA] [DISPLAY] Export ecdsa keys for display purposes
ecdsa_sk1_hex, ecdsa_pk1_hex = ecdsa.export_keys(ecdsa_sk1, ecdsa_pk1)
ecdsa_sk2_hex, ecdsa_pk2_hex = ecdsa.export_keys(ecdsa_sk2, ecdsa_pk2)
print('[ECDSA] [SEED] Private Key 1:', ecdsa_sk1_hex)
print('[ECDSA] [SEED] Public Key 1:', ecdsa_pk1_hex)
print('[ECDSA] [SEED] Private Key 2:', ecdsa_sk2_hex)
print('[ECDSA] [SEED] Public Key 2:', ecdsa_pk2_hex)

# ! [ECDSA] Import the private keys
ecdsa_sk1_from_priv, ecdsa_pk1_from_priv = ecdsa.keypair_gen_privatekey(ecdsa_sk1_hex)
ecdsa_sk2_from_priv, ecdsa_pk2_from_priv = ecdsa.keypair_gen_privatekey(ecdsa_sk2_hex)

# ! [ECDSA] [DISPLAY] Export ecdsa keys for display purposes
ecdsa_sk1_from_priv_hex, ecdsa_pk1_from_priv_hex = ecdsa.export_keys(ecdsa_sk1_from_priv, ecdsa_pk1_from_priv)
ecdsa_sk2_from_priv_hex, ecdsa_pk2_from_priv_hex = ecdsa.export_keys(ecdsa_sk2_from_priv, ecdsa_pk2_from_priv)
print('[ECDSA] [PRIVATE KEY] Private Key 1(from private key):', ecdsa_sk1_from_priv_hex)
print('[ECDSA] [PRIVATE KEY] Public Key 1(from private key):', ecdsa_pk1_from_priv_hex)
print('[ECDSA] [PRIVATE KEY] Private Key 2(from private key):', ecdsa_sk2_from_priv_hex)
print('[ECDSA] [PRIVATE KEY] Public Key 2(from private key):', ecdsa_pk2_from_priv_hex)

# @ [ED25519] Generate ed25519 private keys and public keys
ed25519_sk1, ed25519_pk1 = ed25519.keypair_gen_seed(seed1)
ed25519_sk2, ed25519_pk2 = ed25519.keypair_gen_seed(seed2)

# @ [ED25519] [DISPLAY] Export ed25519 keys for display purposes
ed25519_sk1_hex, ed25519_pk1_hex = ed25519.export_keys(ed25519_sk1, ed25519_pk1)
ed25519_sk2_hex, ed25519_pk2_hex = ed25519.export_keys(ed25519_sk2, ed25519_pk2)
print('[ED25519] [SEED] Private Key 1:', ed25519_sk1_hex)
print('[ED25519] [SEED] Public Key 1:', ed25519_pk1_hex)
print('[ED25519] [SEED] Private Key 2:', ed25519_sk2_hex)
print('[ED25519] [SEED] Public Key 2:', ed25519_pk2_hex)

# % [BLS] Generate a message to sign
message = 'Hello, this is a test message'

# % [BLS] Sign the message with each private key
sig1 = bls.sign(bls_sk1, message)
sig2 = bls.sign(bls_sk2, message)

# % [BLS] [DISPLAY] Export signatures for display purposes
print('[BLS] Signature 1:', utils.export_sig(sig1))
print('[BLS] Signature 2:', utils.export_sig(sig2))

# % [BLS] Generate an aggregated public key and signature
agg_pub_key = bls.aggregateKey([bls_pk1, bls_pk2])
agg_signature = bls.aggregateSig([sig1, sig2])

# % [BLS] [DISPLAY] Export the aggregated public key and signature for display purposes
print('[BLS] Aggregated Public Key:', utils.export_pk(agg_pub_key))
print('[BLS] Aggregated Signature:', utils.export_sig(agg_signature))

# % [BLS] Verify the aggregated signature
verification_result = bls.verify(agg_pub_key, message, agg_signature)

# % [BLS] [DISPLAY] Display the verification result
print('[BLS] Aggregated Signature Verification Result:', verification_result)
assert verification_result, "[BLS] The aggregated signature verification failed!"