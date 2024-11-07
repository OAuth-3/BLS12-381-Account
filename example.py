from util import util
from bls import bls, utils
from ethereum_account import ethereum_account
from bitcoin_account import bitcoin_account
from solana_account import solana_account

# ! [COMMON] Generate multiple private and public key pairs
seed1: bytes = util.create_random(32)
seed2: bytes = util.create_random(32)

# @ [BLS] Generate bls private keys and public keys
bls_sk1, bls_pk1 = bls.keypair_gen_seed(seed1)
bls_sk2, bls_pk2 = bls.keypair_gen_seed(seed2)

# @ [BLS] [DISPLAY] Export keys for display purposes
print('[BLS] [SEED] Private Key 1:', utils.export_sk(bls_sk1))
print('[BLS] [SEED] Public Key 1:', utils.export_pk(bls_pk1))
print('[BLS] [SEED] Private Key 2:', utils.export_sk(bls_sk2))
print('[BLS] [SEED] Public Key 2:', utils.export_pk(bls_pk2))

# @ [BLS] Import the private keys
bls_sk1_from_priv, bls_pk1_from_priv = bls.keypair_gen_privatekey(utils.export_sk(bls_sk1))
bls_sk2_from_priv, bls_pk2_from_priv = bls.keypair_gen_privatekey(utils.export_sk(bls_sk2))

# @ [BLS] [DISPLAY] Export keys for display purposes
print('[BLS] [PRIVATE KEY] Private Key 1:', utils.export_sk(bls_sk1_from_priv))
print('[BLS] [PRIVATE KEY] Public Key 1:', utils.export_pk(bls_pk1_from_priv))
print('[BLS] [PRIVATE KEY] Private Key 2:', utils.export_sk(bls_sk2_from_priv))
print('[BLS] [PRIVATE KEY] Public Key 2:', utils.export_pk(bls_pk2_from_priv))

# # [ETHEREUM] generate ethereum_account keys and address from the seed
ethereum_account_private_key1, ethereum_account_public_key1, ethereum_account_address1 = ethereum_account.keypair_gen_seed(seed1)
ethereum_account_private_key2, ethereum_account_public_key2, ethereum_account_address2 = ethereum_account.keypair_gen_seed(seed2)

# # [ETHEREUM] generate ethereum_account keys and address from the private key
ethereum_account_private_key3, ethereum_account_public_key3, ethereum_account_address3 = ethereum_account.keypair_gen_privatekey(ethereum_account_private_key1)
ethereum_account_private_key4, ethereum_account_public_key4, ethereum_account_address4 = ethereum_account.keypair_gen_privatekey(ethereum_account_private_key2)

# # [ETHEREUM] print the ethereum_account keys and address
print(f'''
[ETHEREUM-ACCOUNT]
SEED-1
    - private key 1: {ethereum_account_private_key1}
    - public key 1: {ethereum_account_public_key1}
    - address 1: {ethereum_account_address1}
SEED-2
    - private key 2: {ethereum_account_private_key2}
    - public key 2: {ethereum_account_public_key2}
    - address 2: {ethereum_account_address2}
PRIVATE KEY-1
    - private key 3: {ethereum_account_private_key3}
    - public key 3: {ethereum_account_public_key3}
    - address 3: {ethereum_account_address3}
PRIVATE KEY-2
    - private key 4: {ethereum_account_private_key4}
    - public key 4: {ethereum_account_public_key4}
    - address 4: {ethereum_account_address4}

------------------------------------------------------------''')

# # [BITCOIN] generate bitcoin_account keys and address from the seed
bitcoin_account_private_key1, bitcoin_account_wif_private_key1, bitcoin_account_public_key1, bitcoin_account_address1 = bitcoin_account.keypair_gen_seed(seed1)
bitcoin_account_private_key2, bitcoin_account_wif_private_key2, bitcoin_account_public_key2, bitcoin_account_address2 = bitcoin_account.keypair_gen_seed(seed2)

# # [BITCOIN] generate bitcoin_account keys and address from the private key
bitcoin_account_private_key3, bitcoin_account_wif_private_key3, bitcoin_account_public_key3, bitcoin_account_address3 = bitcoin_account.keypair_gen_privatekey(False, bitcoin_account_private_key1)
bitcoin_account_private_key4, bitcoin_account_wif_private_key4, bitcoin_account_public_key4, bitcoin_account_address4 = bitcoin_account.keypair_gen_privatekey(False, bitcoin_account_private_key2)

# # [BITCOIN] print the bitcoin_account keys and address
print(f'''
[BITCOIN-ACCOUNT]
SEED-1
    - private key 1: {bitcoin_account_private_key1}
    - wif private key 1: {bitcoin_account_wif_private_key1}
    - public key 1: {bitcoin_account_public_key1}
    - address 1: {bitcoin_account_address1}
SEED-2
    - private key 2: {bitcoin_account_private_key2}
    - wif private key 2: {bitcoin_account_wif_private_key2}
    - public key 2: {bitcoin_account_public_key2}
    - address 2: {bitcoin_account_address2}
PRIVATE KEY-1
    - private key 3: {bitcoin_account_private_key3}
    - wif private key 3: {bitcoin_account_wif_private_key3}
    - public key 3: {bitcoin_account_public_key3}
    - address 3: {bitcoin_account_address3}
PRIVATE KEY-2
    - private key 4: {bitcoin_account_private_key4}
    - wif private key 4: {bitcoin_account_wif_private_key4}
    - public key 4: {bitcoin_account_public_key4}
    - address 4: {bitcoin_account_address4}

------------------------------------------------------------''')

# # [SOLANA] generate solana_account keys and address from the seed
solana_account_private_key1, solana_account_public_key1, solana_account_address1 = solana_account.keypair_gen_seed(seed1)
solana_account_private_key2, solana_account_public_key2, solana_account_address2 = solana_account.keypair_gen_seed(seed2)

# # [SOLANA] generate solana_account keys and address from the private key
solana_account_private_key3, solana_account_public_key3, solana_account_address3 = solana_account.keypair_gen_privatekey(solana_account_private_key1)
solana_account_private_key4, solana_account_public_key4, solana_account_address4 = solana_account.keypair_gen_privatekey(solana_account_private_key2)

# # [SOLANA] print the solana_account keys and address
print(f'''
[SOLANA-ACCOUNT]
SEED-1
    - private key 1: {solana_account_private_key1}
    - public key 1: {solana_account_public_key1}
    - address 1: {solana_account_address1}
SEED-2
    - private key 2: {solana_account_private_key2}
    - public key 2: {solana_account_public_key2}
    - address 2: {solana_account_address2}
PRIVATE KEY-1
    - private key 3: {solana_account_private_key3}
    - public key 3: {solana_account_public_key3}
    - address 3: {solana_account_address3}
PRIVATE KEY-2
    - private key 4: {solana_account_private_key4}
    - public key 4: {solana_account_public_key4}
    - address 4: {solana_account_address4}

------------------------------------------------------------''')

# @ [BLS] Generate a message to sign
message = 'Hello, this is a test message'

# @ [BLS] Sign the message with each private key
sig1 = bls.sign(bls_sk1, message)
sig2 = bls.sign(bls_sk2, message)

# @ [BLS] [DISPLAY] Export signatures for display purposes
print('[BLS] Signature 1:', utils.export_sig(sig1))
print('[BLS] Signature 2:', utils.export_sig(sig2))

# @ [BLS] Generate an aggregated public key and signature
agg_pub_key = bls.aggregateKey([bls_pk1, bls_pk2])
agg_signature = bls.aggregateSig([sig1, sig2])

# @ [BLS] [DISPLAY] Export the aggregated public key and signature for display purposes
print('[BLS] Aggregated Public Key:', utils.export_pk(agg_pub_key))
print('[BLS] Aggregated Signature:', utils.export_sig(agg_signature))

# @ [BLS] Verify the aggregated signature
verification_result = bls.verify(agg_pub_key, message, agg_signature)

# @ [BLS] [DISPLAY] Display the verification result
print('[BLS] Aggregated Signature Verification Result:', verification_result)
assert verification_result, "[BLS] The aggregated signature verification failed!"