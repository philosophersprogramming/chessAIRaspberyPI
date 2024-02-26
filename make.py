from cryptography.fernet import Fernet

# Generate a symmetric encryption key
key = Fernet.generate_key()

# Store the key in a file
with open('encryption_key.key', 'wb') as f:
    f.write(key)
