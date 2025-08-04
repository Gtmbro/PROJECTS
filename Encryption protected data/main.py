import os
import base64
import time
import random

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

file = "secret.bin"

def key_generator(password, salt):
  kdf = PBKDF2HMAC(
    algorithm = hashes.SHA256(),
    length = 32,
    salt = salt,
    iterations = 100000,
    backend = default_backend()
  )
  return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def setup_vault():
  if os.path.exists(file):
    ran_num = random.randint(1,100)
    new_name = f"{os.path.splitext(file)[0]}{ran_num}{os.path.splitext(file)[1]}" 
    os.rename(file,new_name)

  if not os.path.exists(file):
    while True:
      data = input("Enter your data:\n").capitalize()
      if not data:
        print("You haven't added data\n")
        choice = input("Enter 1 to add data:")
        if choice == "1":
          continue
        elif not choice or choice != "1":
          break
        else:
          break

      if data:
        password = input("\nSet the password: ")

        salt = os.urandom(16)
        key = key_generator(password, salt)
        fernet = Fernet(key)

        encrypted = fernet.encrypt(data.encode())

        print("Vault created and data saved successfully!")

        with open(file,'wb') as f:
          f.write(salt+encrypted)
    return data

def load_vault():
  with open(file,'rb') as f:
    read_data = f.read()

  return read_data[:16], read_data[16:]

def unlock_vault():

  saved_salt, encrypted_data = load_vault()
  password_try = input("\nEnter your password: ")

  try:
    key = key_generator(password_try, saved_salt)
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_data).decode()

    return decrypted, fernet, saved_salt

  except:
    print("Wrong password!")
    return None, None, None

def add_entry( decrypted, fernet, saved_salt ):

  new_data = input("\nEnter new data:\n").capitalize()
  combined_data = decrypted + "\n" + new_data
  new_encrypted = fernet.encrypt(combined_data.encode())

  with open(file,'wb') as f:
    f.write(saved_salt+new_encrypted)
  print("\nData added successfully!! ")

def view_vault(decrypted):
   print("\nYour data is:\n" + decrypted)

setup_vault()

error_check = setup_vault()
if not error_check :
  setup_vault()

choice = input("\nEnter 1 to add more data\nEnter 2 to view the stored data:\n")

while choice in ["1", "2"]:

  decrypted, fernet, saved_salt = unlock_vault()

  if choice == "1":
    add_entry( decrypted, fernet, saved_salt )

  elif choice == "2":
    view_vault(decrypted)

  else:
    print("Wrong input!")
    choice2 = input("Enter 1 to do it again\nAnything else to exit: ")
    if choice2 == "1":
      continue
    else:
      break

  if not decrypted:
    choice2 = input("Something is wrong..\nEnter 1 to continue:")
    if choice2 == "1":
      continue
    else:
      print("Wrong choice!\nExiting...")
      for _ in range(1,4):
        print("."*3)
        time.sleep(1)
      break

  choice = input("\nEnter 1 again to add more data\nEnter 2 to view the stored data"
                     "\nAnything else to exit:\n")
