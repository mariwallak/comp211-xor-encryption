from itertools import cycle


def xor_crypt(data: bytes, key: bytes) -> bytes:
    """Encrypts or decrypts a byte sequence using a repeating-key XOR."""
    return bytes(b ^ k for b, k in zip(data, cycle(key)))


# 1. Define plaintext and key
plaintext = "COMP 211: Systems Programming"
key = b"secret_key"

# 2. Encrypt: string -> bytes -> XORed bytes
ciphertext = xor_crypt(plaintext.encode("utf-8"), key)
print(f"Ciphertext (hex): {ciphertext.hex()}")

# 3. Decrypt: XORed bytes -> original bytes -> string
decrypted_bytes = xor_crypt(ciphertext, key)
decrypted_text = decrypted_bytes.decode("utf-8")
print(f"Decrypted text:   {decrypted_text}")
