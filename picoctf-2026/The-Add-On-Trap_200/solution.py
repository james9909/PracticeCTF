from cryptography.fernet import Fernet

f = Fernet(b"cGljb0NURnt5b3UncmUgb24gdGhlIHJpZ2h0IHRyYX0=")
flag = f.decrypt(b"gAAAAABmfRjwFKUB-X3GBBqaN1tZYcPg5oLJVJ5XQHFogEgcRSxSis1e4qwicAKohmjqaD-QG8DIN5ie3uijCVAe3xiYmoEHlxATWUP3DC97R00Cgkw4f3HZKsP5xHewOqVPH8ap9FbE")
print(flag)

"""
Extracting the extension, we see some suspicious strings in background/main.js:

// Secret key must be 32 url-safe base64-encoded bytes!
// TODO I must find a solution to remove the key from here, for now I'll leave it there because I need it to encrypt the webhook

function logOnCompleted(details) {
    console.log(`Information to exfiltrate: ${details.url}`);
    const key="cGljb0NURnt5b3UncmUgb24gdGhlIHJpZ2h0IHRyYX0="
    const webhookUrl='gAAAAABmfRjwFKUB-X3GBBqaN1tZYcPg5oLJVJ5XQHFogEgcRSxSis1e4qwicAKohmjqaD-QG8DIN5ie3uijCVAe3xiYmoEHlxATWUP3DC97R00Cgkw4
f3HZKsP5xHewOqVPH8ap9FbE'

Looking up 32 url-safe base64-encoded bytes in python, we see the Fernet cryptography scheme
which uses a key of that format to encrypt/decrypt bytes.

picoCTF{Us3_4dd/0ns_v3ry_c4r3fully1}
"""
