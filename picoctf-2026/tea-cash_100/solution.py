from pwn import *

NUM_CHUNKS = 6
CHUNK_SIZE = 0x80
OFFSET = 16

r = remote("candy-mountain.picoctf.net", 55805)
head = r.recvline().decode()
head = int(head[head.find("0x")+2:], 16)
print(f"Base: {hex(head)}")
for i in range(NUM_CHUNKS):
    print(r.recv())
    r.sendline(hex(head + (i * (CHUNK_SIZE + OFFSET))).encode())
print(r.recvall())

"""
This problem requires us to traverse the linked list that was malloc'd and then freed. We're given the
address for the head of the list so we can calculate the next addresses based on the size of the chunks (0x80).

Each chunk is also offset by 0x10 (2 pointers), so we just need to add that to our calculations to compute every address.

$ python3 solution.py
[+] Opening connection to candy-mountain.picoctf.net on port 55805: Done
Base: 0xa551490
b'Chunk 1 address: '
b'Chunk 2 address: '
b'Chunk 3 address: '
b'Chunk 4 address: '
b'Chunk 5 address: '
b'Chunk 6 address: '
[+] Receiving all data: Done (67B)
[*] Closed connection to candy-mountain.picoctf.net port 55805
b'Correct traversal! Flag: picoCTF{0fd522cb3e9905002631d25e21a4750b}\n'
picoCTF{0fd522cb3e9905002631d25e21a4750b}
"""
