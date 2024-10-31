from bls import bls, utils
from ecdsa import ecdsa

# % [BLS] Generate multiple private and public key pairs
seed1: bytes = bytes([0,  50, 6,  244, 24,  199, 1,  25,  52,  88,  192, 19, 18, 12, 89,  6,   220, 18, 102, 58,  209, 82, 12, 62, 89, 110, 182, 9,   44, 20,  254, 22])
seed2: bytes = bytes([1,  60, 16, 214, 34,  179, 15,  28,  92,  118, 234, 33, 29, 22, 78,  9,   200, 28, 142, 78,  209, 90, 16, 66, 85, 150, 132, 5,   45, 25,  244, 35])

# % [BLS] Generate bls private keys and public keys
bls_sk1, bls_pk1 = bls.keypair_gen_seed(seed1)
bls_sk2, bls_pk2 = bls.keypair_gen_seed(seed2)

# @ [BLS] [DISPLAY] Export keys for display purposes
print('BLS Private Key 1:', utils.export_sk(bls_sk1))
print('BLS Public Key 1:', utils.export_pk(bls_pk1))
print('BLS Private Key 2:', utils.export_sk(bls_sk2))
print('BLS Public Key 2:', utils.export_pk(bls_pk2))

# % [BLS] Import the private keys
bls_sk1_from_priv, bls_pk1_from_priv = bls.keypair_gen_privatekey(utils.export_sk(bls_sk1))
bls_sk2_from_priv, bls_pk2_from_priv = bls.keypair_gen_privatekey(utils.export_sk(bls_sk2))
print('BLS Private Key 1(from private key):', utils.export_sk(bls_sk1_from_priv))
print('BLS Public Key 1(from private key):', utils.export_pk(bls_pk1_from_priv))
print('BLS Private Key 2(from private key):', utils.export_sk(bls_sk2_from_priv))
print('BLS Public Key 2(from private key):', utils.export_pk(bls_pk2_from_priv))

# ! [ECDSA] Generate ecdsa private keys and public keys
ecdsa_sk1, ecdsa_pk1 = ecdsa.keypair_gen_seed(seed1)
ecdsa_sk2, ecdsa_pk2 = ecdsa.keypair_gen_seed(seed2)

# @ [ECDSA] [DISPLAY] Export ecdsa keys for display purposes
ecdsa_sk1_hex, ecdsa_pk1_hex = ecdsa.export_keys(ecdsa_sk1, ecdsa_pk1)
ecdsa_sk2_hex, ecdsa_pk2_hex = ecdsa.export_keys(ecdsa_sk2, ecdsa_pk2)
print('ECDSA Private Key 1:', ecdsa_sk1_hex)
print('ECDSA Public Key 1:', ecdsa_pk1_hex)
print('ECDSA Private Key 2:', ecdsa_sk2_hex)
print('ECDSA Public Key 2:', ecdsa_pk2_hex)

ecdsa_sk1_from_priv, ecdsa_pk1_from_priv = ecdsa.keypair_gen_privatekey(ecdsa_sk1_hex)
ecdsa_sk2_from_priv, ecdsa_pk2_from_priv = ecdsa.keypair_gen_privatekey(ecdsa_sk2_hex)
ecdsa_sk1_hex_from_priv, ecdsa_pk1_hex_from_priv = ecdsa.export_keys(ecdsa_sk1_from_priv, ecdsa_pk1_from_priv)
ecdsa_sk2_hex_from_priv, ecdsa_pk2_hex_from_priv = ecdsa.export_keys(ecdsa_sk2_from_priv, ecdsa_pk2_from_priv)
print('ECDSA Private Key 1(from private key):', ecdsa_sk1_hex_from_priv)
print('ECDSA Public Key 1(from private key):', ecdsa_pk1_hex_from_priv)
print('ECDSA Private Key 2(from private key):', ecdsa_sk2_hex_from_priv)
print('ECDSA Public Key 2(from private key):', ecdsa_pk2_hex_from_priv)

# % [BLS] Generate a message to sign
message = 'Hello, this is a test message'

# % [BLS] Sign the message with each private key
sig1 = bls.sign(bls_sk1, message)
sig2 = bls.sign(bls_sk2, message)

# @ [BLS] [DISPLAY] Export signatures for display purposes
print('Signature 1:', utils.export_sig(sig1))
print('Signature 2:', utils.export_sig(sig2))

# % [BLS] Generate an aggregated public key and signature
agg_pub_key = bls.aggregateKey([bls_pk1, bls_pk2])
agg_signature = bls.aggregateSig([sig1, sig2])

# @ [BLS] [DISPLAY] Export the aggregated public key and signature for display purposes
print('Aggregated Public Key:', utils.export_pk(agg_pub_key))
print('Aggregated Signature:', utils.export_sig(agg_signature))

# % [BLS] Verify the aggregated signature
verification_result = bls.verify(agg_pub_key, message, agg_signature)

# @ [BLS] [DISPLAY] Display the verification result
print('Aggregated Signature Verification Result:', verification_result)
assert verification_result, "The aggregated signature verification failed!"
