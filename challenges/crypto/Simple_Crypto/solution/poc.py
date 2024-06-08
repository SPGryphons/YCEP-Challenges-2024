import requests
import base64

HOST_IP = '127.0.0.1'
PORT = 5000
URL = f'http://{HOST_IP}:{PORT}'

KEY = "supersecretkey"


def xor_encrypt(message, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(message))


def encrypt(message):
    return base64.b64encode(xor_encrypt(message, KEY).encode()).decode()


def decrypt(encrypted_message):
    return xor_encrypt(base64.b64decode(encrypted_message).decode(), KEY)


def get_encrypted_key():
    try:
        response = requests.post(f'{URL}/send', json={"message": "Key to GET Flag"})
        response.raise_for_status()
        response_data = response.json()
        encrypted_message = response_data.get("encrypted_message")
        return encrypted_message
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except ValueError as e:
        print(f"JSON decoding failed: {e}")
    return None


def get_flag(decrypted_key):
    try:
        response = requests.post(f'{URL}/receive', json={"message": decrypted_key})
        response.raise_for_status()
        response_data = response.json()
        flag_message = response_data.get("message")
        return flag_message
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except ValueError as e:
        print(f"JSON decoding failed: {e}")
        print(f"Raw response content: {response.text}")
    return None


if __name__ == "__main__":
    # Step 1: Get the encrypted key
    encrypted_key = get_encrypted_key()
    if encrypted_key:
        print("Encrypted key:", encrypted_key)

        # Step 2: Decrypt the encrypted key
        decrypted_key = decrypt(encrypted_key)
        print("Decrypted key:", decrypted_key)

        # Step 3: Use the decrypted key to get the flag
        flag = get_flag(decrypted_key)
        if flag:
            print("Flag:", flag)
        else:
            print("Failed to retrieve the flag.")
    else:
        print("Failed to retrieve the encrypted key.")
