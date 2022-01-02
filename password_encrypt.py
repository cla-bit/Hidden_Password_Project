from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)
        print('Key is generated')


# generate_key()


def load_key():
    return open('secret.key', 'rb').read()


def encrypt_key():
    key = load_key()
    message = input('Enter your text to encrypt: ')
    encode_msg = message.encode()
    f = Fernet(key)
    encrypt_msg = f.encrypt(encode_msg)
    return encrypt_msg


def decrypt_key(msg):
    key = load_key()
    f = Fernet(key)
    decrypt_msg = f.decrypt(msg)
    decrypt_message = decrypt_msg.decode()
    return decrypt_message


v = encrypt_key()
print(v, len(v))
print()
print(decrypt_key(v))
print(len(decrypt_key(v)))
