import json

with open("incidents.json") as f:
    incidents = json.load(f)

src = {}
dst = {}
files = {}
for ticket in incidents["tickets"]:
    file_hash = ticket["file_hash"]
    src_ip = ticket["src_ip"]
    dst_ip = ticket["dst_ip"]

    if src_ip in src:
        src[src_ip] += 1
    else:
        src[src_ip] = 1

    if src_ip in dst:
        dst[src_ip].add(dst_ip)
    else:
        dst[src_ip] = set([dst_ip])

    if file_hash in files:
        files[file_hash].add(dst_ip)
    else:
        files[file_hash] = set([dst_ip])

print(max(src, key=lambda x: src[x]))
print(len(dst["6.19.128.119"]))

avg = 0.0
for f in files:
    avg += len(files[f])
avg /= len(files)
print(avg)

# picoCTF{J4y_s0n_d3rUUUULo_c74e3495}
