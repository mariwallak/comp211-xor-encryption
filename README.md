# Simple Encryption Using XOR

This repository documents an exploration of simple encryption using the bitwise Exclusive-OR (XOR) operator for COMP 211 Checkoff 3. It explores how a bitwise operation can serve as a cipher, how it is reversible, and why repeating-key methods are insecure.

## What Was Explored

* **Mathematical Foundations:** The algebraic properties of the bitwise XOR operator, focusing on ($A \oplus A = 0$) and symmetry ($\text{Plaintext} \oplus \text{Key} = \text{Ciphertext}$).
* **Manual Binary Tracing:** Step-by-step bit-level tracking using ASCII characters (such as `'A'` and `'K'`) to verify how decryption restores original data.
* **Python Implementation:** Writing a script to handle byte-level XOR and repeating-key indexing.
* **Security Analysis:** Investigating why XOR is vulnerable to known-plaintext attacks.

## Most Interesting Discoveries

* **The Toggle Switch Property:** XOR acts as a two-way bit mask. Applying the key once toggles specific bits to encrypt it, and applying the exact same key a second time restores the original data with zero loss (decrypts perfectly).
* **Vulnerability to Key Reuse:** With repeating keys, an interceptor can easily recover the key using known-plaintext attacks ($\text{Plaintext} \oplus \text{Ciphertext} = \text{Key}$).
* **Foundation of Modern Ciphers:** While standalone repeating-key XOR is insecure, XOR is the core engine inside modern protocols like AES and ChaCha20 which use random key generators.

## Code Example & Execution

This project includes a Python script (`xor_encryption.py`) demonstrating repeating-key XOR encryption and decryption.

### How to Run:
1. Ensure Python 3 is installed.
2. Run the script from your terminal:
   ```bash
   python3 xor_encryption.py

## Additional Resources
- COMP 211 Course Materials on Bitwise Operators (`&`, `|`, `^`, `~`)
- Claude Shannon, *Communication Theory of Secrecy Systems* (Mathematical foundations of symmetric ciphers and the One-Time Pad)
- Python Standard Library Documentation (`itertools.cycle`, `bytes`)
