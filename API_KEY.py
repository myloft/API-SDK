import requests
import getpass

username = input("Please input your username:")
password = getpass.getpass("Please input your password:")

payload = {'username': username, 'password': password}

r = requests.post("https://api.iloft.xyz/login", data=payload)

print("Your JSON Web Tokens is:")
print(r.text)
