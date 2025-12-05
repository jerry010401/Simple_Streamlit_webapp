from cryptography.fernet import Fernet

# class to prevent accidental print / log of password
class FakeStr(str):
    def __str__(self):
        return "****"
    def __repr__(self):
        return "****"

# load the Secret key
def load_key():
    return open("secret_key.txt", "rb").read()

# Encrypt the plain password
def encrypt_password(password: str) -> bytes:
    key = load_key()
    f = Fernet(key)
    return f.encrypt(password.encode())

# Decrypt the password and return a protected string
def decrypt_password(encrypted_password: bytes) -> FakeStr:
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_password).decode()
    return FakeStr(decrypted)

# final method to call from app
def get_decrypted_password() -> FakeStr:
    # This is the encrypted token, not the secret key
    encrypted_password = b'gAAAAABpLU0oxCSAWAiiXjCuQq9GpTC7gqpCeXROfoeMJgUMwiGDlgFKjEjnnTKkQBZhuYVI09-gCJBoOUxDLKc7jpXfDG7EDQ=='
    return decrypt_password(encrypted_password)