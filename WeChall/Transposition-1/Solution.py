ciphertext = "oWdnreuf.lY uoc nar ae dht eemssga eaw yebttrew eh nht eelttre sra enic roertco drre . Ihtni koy uowlu dilekt  oes eoyrup sawsro don:wl defcirbros.i"

decoded = ""
i = 0
while (i+1 < len(ciphertext)):
    decoded += ciphertext[i+1] + ciphertext[i]
    i += 2

print decoded
