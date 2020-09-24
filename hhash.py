
import hashlib

password = input()
username = input()
password += username
h = hashlib.md5(password.encode())
password = h.hexdigest() + "museum"
h = hashlib.md5(password.encode())
password = "md5" + h.hexdigest()
print(password)
