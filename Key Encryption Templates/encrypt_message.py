import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def utf8(s: bytes):
    return str(s, 'utf-8')

def load_public_key(file_name):
    with open(file_name, 'rb') as file:
        public_key_data = file.read()
        public_key = serialization.load_pem_public_key(public_key_data, backend=default_backend())
    return public_key

def encrypt_message(msg, key):
    encrypted_msg = base64.b64encode(key.encrypt(
        msg,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    ))
    return encrypted_msg # Returns bytes


def main():
    # Obtain the value of the public key
    public_key = load_public_key('X_my_public_key.pem')

    # Create a secret message
    message = b'This is my secret message!'
    print(f'Unencrypted:\n{utf8(message)}\n\n')

    # Encrypt the message
    encrypted_msg = encrypt_message(message, public_key)

    print(f'Encrypted:\n{utf8(encrypted_msg)}\n\n')

    # Write the encrypted message to a file
    with open('XX_encrypted_message.bin', 'wb') as file:
        file.write(encrypted_msg)

if __name__ == "__main__":
    main()