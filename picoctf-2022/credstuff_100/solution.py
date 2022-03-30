import codecs

usernames = open("leak/usernames.txt", "r").readlines()
passwords = open("leak/passwords.txt", "r").readlines()

for username, password in zip(usernames, passwords):
    username = username.strip()
    password = password.strip()
    if username == "cultiris":
        print(codecs.encode(password, "rot_13"))

# picoCTF{C7r1F_54V35_71M3}
