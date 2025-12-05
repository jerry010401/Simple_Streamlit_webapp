from password_utils import encrypt_password

from cryptography.fernet import Fernet

# generate key and save file.
def generate_key():
    key = Fernet.generate_key()
    with open("secret_key.txt","wb")as file:
        file.write(key)
        print(" Key save to 'secret_key!'")

if __name__ == "__main__":
    # uncomment this only first time after run do comment this.
    generate_key()

    # replace your real mySql root password....
    encrypted = encrypt_password("root")
    print("Encrypted password (copy this to password_utils.py):")
    print(encrypted)




