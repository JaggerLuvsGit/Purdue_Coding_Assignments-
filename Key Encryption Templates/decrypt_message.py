import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def utf8(s: bytes):
    return str(s, 'utf-8')
        
def load_private_key(file_name):
    with open(file_name, 'rb') as file:
        private_key_data = file.read()
        private_key = serialization.load_pem_private_key(private_key_data, password=None, backend=default_backend())
    return private_key

def load_private_key_enc(file_name, password):
    private_key_pass = password
    with open(file_name, 'rb') as file:
        private_key_data = file.read()
        private_key = serialization.load_pem_private_key(private_key_data, password=private_key_pass, backend=default_backend())
    return private_key

def decrypt_message(msg, key):
    decrypted_msg = key.decrypt(
    base64.b64decode(msg),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_msg

def main():
    # Obtain the value of the private key
    # This would normally be stored somewhere on your hard drive
    private_key = load_private_key('X_my_private_key.pem')

    # Load the encrypted message from the file
    with open('XX_encrypted_message.bin', 'rb') as file:
        encrypted_data = file.read()

    # Decrypt the message
    decrypted_msg = decrypt_message(encrypted_data, private_key)

    print(f'Decrypted using private key:\n{utf8(decrypted_msg)}\n\n')


    # Obtain the value of the private key
    # This would normally be stored somewhere on your hard drive
    private_key_pass = b"I LiKe THiS P@ssWerd##"
    private_key = load_private_key_enc('X_my_private_key_enc.pem',private_key_pass)

    # Load the encrypted message from the file
    with open('XX_encrypted_message.bin', 'rb') as file:
        encrypted_data = file.read()

    # Decrypt the message
    decrypted_msg = decrypt_message(encrypted_data, private_key)

    print(f'Decrypted using encrypted private key:\n{utf8(decrypted_msg)}\n\n')

if __name__ == "__main__":
    main()