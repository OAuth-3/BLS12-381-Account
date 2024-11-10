from util import util
from bls import bls
from ethereum_account import ethereum_account
from bitcoin_account import bitcoin_account
from solana_account import solana_account

# ! [COMMON] generate random seeds
seed1: bytes = util.create_random(32)
seed2: bytes = util.create_random(32)

# @ [BLS] generate bls keys from the seed
bls_private_key1, bls_public_key1 = bls.keypair_gen_seed(seed1)
bls_private_key2, bls_public_key2 = bls.keypair_gen_seed(seed2)

# @ [BLS] generate bls keys from the private key
bls_private_key3, bls_public_key3 = bls.keypair_gen_privatekey(bytes(bls_private_key1).hex())
bls_private_key4, bls_public_key4 = bls.keypair_gen_privatekey(bytes(bls_private_key2).hex())

# @ [BLS] print the bls keys
print(f'''
[BLS]
SEED-1
    - private key 1: {bytes(bls_private_key1).hex()}
    - public key 1: {bytes(bls_public_key1).hex()}
SEED-2
    - private key 2: {bytes(bls_private_key2).hex()}
    - public key 2: {bytes(bls_public_key2).hex()}
PRIVATE KEY-1
    - private key 3: {bytes(bls_private_key3).hex()}
    - public key 3: {bytes(bls_public_key3).hex()}
PRIVATE KEY-2
    - private key 4: {bytes(bls_private_key4).hex()}
    - public key 4: {bytes(bls_public_key4).hex()}

------------------------------------------------------------''')

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

------------------------------------------------------------
''')

# @ [BLS] Generate a message to sign
message = 'Hello, this is a test message'

# @ [BLS] Sign the message with each private key
sig1 = bls.sign(bls_private_key1, message)
sig2 = bls.sign(bls_private_key2, message)

# @ [BLS] [DISPLAY] Export signatures for display purposes
print('[BLS] Signature 1:', bytes(sig1).hex())
print('[BLS] Signature 2:', bytes(sig2).hex())

# @ [BLS] Generate an aggregated public key and signature
agg_pub_key = bls.aggregateKey([bls_public_key1, bls_public_key2])
agg_signature = bls.aggregateSig([sig1, sig2])

# @ [BLS] [DISPLAY] Export the aggregated public key and signature for display purposes
print('[BLS] Aggregated Public Key:', bytes(agg_pub_key).hex())
print('[BLS] Aggregated Signature:', bytes(agg_signature).hex())

# @ [BLS] Verify the aggregated signature
verification_result = bls.verify(agg_pub_key, message, agg_signature)

# @ [BLS] [DISPLAY] Display the verification result
print('[BLS] Aggregated Signature Verification Result:', verification_result)
assert verification_result, "[BLS] The aggregated signature verification failed!"