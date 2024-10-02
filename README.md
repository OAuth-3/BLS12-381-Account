
# BLS Signature Scheme Example

This project demonstrates how to use BLS (Boneh-Lynn-Shacham) signatures with Python to sign messages, aggregate signatures and public keys, and verify the aggregated signature.

## Prerequisites

Ensure that you have Python 3 installed. You will also need the following libraries:

- `bls` – BLS library for key generation, signing, and verification
- `utils` – Utility functions for handling key, signature import/export and encoding

## Project Structure

```
bls12-381/
│
├── bls/
│   ├── __init__.py    # Initializes the BLS module
│   ├── bls.py         # Main functions for signing, verifying, and aggregating keys and signatures
│   ├── utils.py       # Utility functions for key/signature handling and conversions
│   └── ...            # Other helper modules
├── example.py         # Main example script to demonstrate BLS signature process
└── README.md          # Project documentation
```

## Steps to Run the Example

### 1. Clone the Repository

```bash
git clone https://github.com/oauth3web3/bls12-381
cd bls-signature-example
```

### 2. Run the Example Script

The example script generates two key pairs, signs a message, aggregates the keys and signatures, and then verifies the aggregated signature.

Run the script:

```bash
python3 example.py
```

### 3. Understanding the Code

#### Key Generation

The example uses the `bls.key_gen()` function to generate private and public key pairs from a seed.

```python
sk1, pk1 = bls.key_gen(seed1)
sk2, pk2 = bls.key_gen(seed2)
```

#### Signing the Message

Each private key is used to sign a common message. This is done using the `bls.sign()` function:

```python
sig1 = bls.sign(sk1, message)
sig2 = bls.sign(sk2, message)
```

#### Aggregating Keys and Signatures

Once the signatures are created, they are aggregated along with their public keys using the following aggregation methods:

```python
agg_pub_key = bls.aggregateKey([pk1, pk2])
agg_signature = bls.aggregateSig([sig1, sig2])
```

#### Verifying the Aggregated Signature

To verify the aggregated signature, we use the `bls.verify()` method:

```python
verification_result = bls.verify(agg_pub_key, message, agg_signature)
```

If the verification is successful, the result will be `True`.

### 4. Output Example

When you run the `example.py` script, you will see output similar to the following:

```
Private Key 1: 377091f0e728463bc2da7d546c53b9f6b81df4a1cc1ab5bf29c5908b7151a32d
Public Key 1: 86243290bbcbfd9ae75bdece7981965350208eb5e99b04d5cd24e955ada961f8c0a162dee740be7bdc6c3c0613ba2eb1
Private Key 2: 3f571a83c18225b6b1d2de5607b0ba4e60ffa5c81b27b36ab38c9d950db55cff
Public Key 2: 8affc168d8c7e1dc603cabb69701df745bd8917e88dec87094de5617978040bba2add86a962d0d58d429ea3e362e1575
Signature 1: <hex-encoded-signature-1>
Signature 2: <hex-encoded-signature-2>
Aggregated Public Key: <hex-encoded-aggregated-public-key>
Aggregated Signature: <hex-encoded-aggregated-signature>
Aggregated Signature Verification Result: True
```

### 5. Error Handling

In case you encounter the following error:

```
TypeError: encoding without a string argument
```

Make sure that the `message` passed to `bls.sign()` is in bytes format, as demonstrated in the example.

### 6. Explanation of Utility Functions

#### `to_bytes()`

Converts a string or bytes input into bytes. It handles string-to-bytes conversion and avoids re-encoding data already in bytes format.

```python
def to_bytes(data):
    if isinstance(data, bytes):
        return data  # Return if it's already bytes
    elif isinstance(data, str):
        return bytes(data, 'utf-8')  # Convert string to bytes
    else:
        raise TypeError(f"Unsupported data type {type(data)}, expected str or bytes.")
```

This function is called before signing to ensure that the message is properly encoded.

---

### 7. Next Steps

You can extend this example by:
- Adding more key pairs and signatures.
- Testing with different messages.
- Exploring additional cryptographic features like threshold signatures or multi-party signing.

---

### License

This project is licensed under the MIT License.
