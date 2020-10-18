import socket
from z3 import *

HOST = "misc.chal.csaw.io"
PORT = 9002

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
print(sock.recv(1024))

def solve(exp):
    s = Solver()
    X = Real("X")
    eval("s.add({})".format(exp.replace("=", "==")), {"s": s, "X": X})
    s.check()
    value = s.model()[X]
    if is_rational_value(value):
        return float(value.numerator_as_long()) / float(value.denominator_as_long())
    return value

while True:
    prompt = sock.recv(1024)
    print(prompt)
    prompt = prompt.replace("YAAAAAY keep going\n", "")

    expr = prompt.split("\n")[0]
    value = solve(expr)
    print(value)
    sock.send(str(value) + "\n")
