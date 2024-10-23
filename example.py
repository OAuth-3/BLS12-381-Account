from bls import bls, utils
from ecdsa import ecdsa

# Step 1: Generate multiple private and public key pairs
seed1: bytes = bytes([0,  50, 6,  244, 24,  199, 1,  25,  52,  88,  192, 19, 18, 12, 89,  6,   220, 18, 102, 58,  209, 82, 12, 62, 89, 110, 182, 9,   44, 20,  254, 22])
seed2: bytes = bytes([1,  60, 16, 214, 34,  179, 15,  28,  92,  118, 234, 33, 29, 22, 78,  9,   200, 28, 142, 78,  209, 90, 16, 66, 85, 150, 132, 5,   45, 25,  244, 35])

# Generate bls private keys and public keys
bls_sk1, bls_pk1 = bls.key_gen(seed1)
bls_sk2, bls_pk2 = bls.key_gen(seed2)

# Export keys for display purposes
print('BLS Private Key 1:', utils.export_sk(bls_sk1))
print('BLS Public Key 1:', utils.export_pk(bls_pk1))
print('BLS Private Key 2:', utils.export_sk(bls_sk2))
print('BLS Public Key 2:', utils.export_pk(bls_pk2))

# Generate ecdsa private keys and public keys
ecdsa_sk1, ecdsa_pk1 = ecdsa.generate_ecdsa_key_pair(seed1)
ecdsa_sk2, ecdsa_pk2 = ecdsa.generate_ecdsa_key_pair(seed2)

# Export keys for display purposes
ecdsa_sk1_hex, ecdsa_pk1_hex = ecdsa.export_ecdsa_keys(ecdsa_sk1, ecdsa_pk1)
ecdsa_sk2_hex, ecdsa_pk2_hex = ecdsa.export_ecdsa_keys(ecdsa_sk2, ecdsa_pk2)

print('ECDSA Private Key 1:', ecdsa_sk1_hex)
print('ECDSA Public Key 1:', ecdsa_pk1_hex)
print('ECDSA Private Key 2:', ecdsa_sk2_hex)
print('ECDSA Public Key 2:', ecdsa_pk2_hex)

# Step 2: Sign a message using both private keys
message = b'Hello, this is a test message'

# Sign the message with each private key
sig1 = bls.sign(bls_sk1, message)
sig2 = bls.sign(bls_sk2, message)

# Export signatures for display purposes
print('Signature 1:', utils.export_sig(sig1))
print('Signature 2:', utils.export_sig(sig2))

# Step 3: Aggregate public keys and signatures
agg_pub_key = bls.aggregateKey([bls_pk1, bls_pk2])
agg_signature = bls.aggregateSig([sig1, sig2])

# Export aggregated key and signature
print('Aggregated Public Key:', utils.export_pk(agg_pub_key))
print('Aggregated Signature:', utils.export_sig(agg_signature))

# Step 4: Verify the aggregated signature
verification_result = bls.verify(agg_pub_key, message, agg_signature)
print('Aggregated Signature Verification Result:', verification_result)

assert verification_result, "The aggregated signature verification failed!"
