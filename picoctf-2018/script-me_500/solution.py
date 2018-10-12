from pwn import *

class Atom:

    def __init__(self, s):
        self.s = s.strip()

    def __add__(self, other):
        my_weight = self.weight
        other_weight = other.weight
        if my_weight < other_weight:
            # Get absorbed by the other atom
            s = "(" + self.s + other.s[1:]
        elif my_weight > other_weight:
            # Absorb the other atom
            s = self.s[:-1] + other.s + ")"
        else:
            # Combine
            s = self.s + other.s
        return Atom(s)

    @property
    def weight(self):
        ret = 0
        curr = 0
        for char in self.s:
            if char == "(":
                curr += 1
                ret = max(ret, curr)
            elif char == ")":
                curr -= 1
        return max(ret, curr)

    def __repr__(self):
        return self.s

    def __eq__(self, other):
        return self.s == other.s

    def __str__(self):
        return self.s


def evaluate(expression):
    expression = expression.split(" + ")
    atoms = [Atom(s) for s in expression]
    return str(reduce(lambda x, y: x + y, atoms))

assert evaluate("() + ()") == "()()" # combine
assert evaluate("((())) + ()") == "((())())" # absorb right
assert evaluate("() + ((()))") == "(()(()))" # absorb left
assert evaluate("(())(()) + ()") == "(())(()())" # combined absorb right
assert evaluate("() + (())(())") == "(()())(())" # combined absorb left
assert evaluate("(())(()) + ((()))") == "((())(())(()))" # absorb combined right
assert evaluate("((())) + (())(())") == "((())(())(()))" # absorb combined left
assert evaluate("() + (()) + ((()))") == "((()())(()))" # left associative

r = remote("2018shell3.picoctf.com", 8672)
for x in range(14):
    print(r.recvline().strip())

while True:
    prompt = r.recvline().strip()
    print("Prompt: {}".format(prompt))
    prompt = prompt[:prompt.index("=")]
    ans = str(evaluate(prompt))
    print(ans)
    r.sendline(ans)
    print(r.recvline().strip())
    print(r.recvline().strip())
    print(r.recvline().strip())
    last = r.recvline().strip()
    print(last)
    if "picoCTF" in last:
        break

"""
The rules seem pretty straightfoward. If the weight of one atom is greater than the other, then
the atom with the larger weight absorbs the one with the smaller weight. Otherwise they're just
concatenated together.

The weight of an atom is determined by the maximum level of nesting that occurs within it.

picoCTF{5cr1pt1nG_l1k3_4_pRo_0970eb2d}
"""
