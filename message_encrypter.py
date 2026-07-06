from cryptography.fernet import Fernet

key = Fernet.generate_key()
fer = Fernet(key)
line = "=========================================================================================="
print(line)
print(f"=================MESAGE ENCRYPTER 1.1.======================== \n ----------------By-Yar-Muhamad---------------------------------- \n {line}")
user_message = input("Enter Text here: ")
print(line)
token = fer.encrypt(user_message.encode('utf-8'))
d_msg = f"Your message is: {fer.decrypt(token)}"
e_msg = f"Your encrypted message is: {token}"


print(line)
print("================SUCESFUL==================================================================")
print(line)
print(d_msg)
print(e_msg)
print(line)