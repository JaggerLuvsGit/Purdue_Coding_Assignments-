from cryptography.hazmat.primitives.asymmetric import rsa 
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def generate_private_key():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
        backend=default_backend()
    )
    return private_key
#function to make a public key from the private key
def generate_public_key(private_key):
    public_key = private_key.public_key()
    return public_key

def write_private_key_to_file(file_name, private_key):
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    with open(file_name, 'wb') as f:
        f.write(private_pem)
# if you do this one with encryption you must add PW to allow it to be decrypted
def write_private_key_to_file_encrypted(file_name, private_key):
    private_key_pass = b"I LiKe THiS P@ssWerd##"
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(private_key_pass)
    )
    with open(file_name, 'wb') as f:
        f.write(private_pem)


def write_public_key_to_file(file_name, public_key):
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open(file_name, 'wb') as f:
        f.write(public_pem)

def main():
    # Generate a new private key
    private_key = generate_private_key()

    # Generate a new public key
    public_key = generate_public_key(private_key)

    # Write private key to file
    write_private_key_to_file('X_my_private_key.pem', private_key)

    # Write public key to file
    write_public_key_to_file('X_my_public_key.pem', public_key)

    # Write private key to file
    write_private_key_to_file_encrypted('X_my_private_key_enc.pem', private_key)

if __name__ == "__main__":
    main()