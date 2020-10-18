import collections
import socket
import string

HOST = "crypto.chal.csaw.io"
PORT = 8042
CHARSET = string.ascii_lowercase + "_"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
sock.recv(1024)

def send(candidate):
    sock.send(candidate + "\n")
    data = sock.recv(1024).replace("\nEncrypting service\n", "").strip("\n")
    return ord(data[-1])

def mode(l):
    c = collections.Counter(l)
    return c.most_common(1)[0][0]

def try_line(suffix):
    print(suffix)
    samples = {}
    for char in CHARSET:
        candidate = char + suffix
        actual = candidate
        while len(actual) < 20:
            actual += candidate
        samples[candidate] = send(actual)
    m = mode(samples.values())
    print(samples)
    for k in samples:
        if samples[k] == m:
            continue
        try_line(k)

try_line("crime_doesnt_have_a_logo")
