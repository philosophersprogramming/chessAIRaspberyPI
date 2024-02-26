from cryptography.fernet import Fernet

def decode():
# Load the key used for encryption
    with open('encryption_key.key', 'rb') as f:
        key = f.read()

    # Load the encrypted token from the file
    with open('oauth_token.pickle', 'rb') as f:
        encrypted_token = f.read()

    cipher_suite = Fernet(key)
    decrypted_token = cipher_suite.decrypt(encrypted_token).decode()

    return decrypted_token
    # Now you can use decrypted_token in your program
