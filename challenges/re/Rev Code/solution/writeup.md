# Solution

1. Run this solve.py script to decrypt the flag.
```
from cryptography.fernet import Fernet

encrypted_flag = b'gAAAAABmYAyviDpizYYTipF3WYnazGf-xMr7FMYMeTzv8raBDL3m5XeGIy3lbVEquB9oYyN4u_4AzLu9bMJXO-EfY5dJWgi7zt5zGswbmfE6Ho2iFvOMTG7-rKIM6Snk3-3lSPWygaFi'
key = b'UzCP0BWCLgd1kTX25dqHCOGUyttLPgXwB6dBrDybco4='
cipher_suite = Fernet(key)

def decrypt(message):
    """Decrypt a token."""
    return cipher_suite.decrypt(message)

# Decrypting the flag
decrypted_flag = decrypt(encrypted_flag)
print(f'Decrypted: {decrypted_flag.decode()}')
```

* It will output the flag: ```YCEP24{S1mp13_W4y_7o_r3v3rEs_c06e_mas92narfa}```

Flag: ```YCEP24{S1mp13_W4y_7o_r3v3rEs_c06e_mas92narfa}```