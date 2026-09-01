enc = "}1a9ftc_oc_ipb50aftc_oc_ip8_99ftc_oc_ip9_TGftc_oc_ip_xehftc_oc_ip_tigftc_oc_ipid_3ftc_oc_ip{FTCftc_oc_ipocipftc_oc_ip"

enc = enc[::-1]
enc = enc.replace("pi_co_ctf", "")
print(enc)

"""
Reversing the binary and analyzing the main function, we see that the program requires a decimal or hexadecimal larger than
999 but less than 10000. The number must also be exactly 3 digits. We can't do this with base 10, so let's use hex.

$ python3
>>> hex(1000)
'0x3e8'

> nc green-hill.picoctf.net 53073
Enter a numeric code (must be > 999 ): 3e8
Access granted: }1a9ftc_oc_ipb50aftc_oc_ip8_99ftc_oc_ip9_TGftc_oc_ip_xehftc_oc_ip_tigftc_oc_ipid_3ftc_oc_ip{FTCftc_oc_ipocipftc_oc_ip

The output is some encoded version of the flag. Looking at the implementation of reveal_flag, we see that the flag is printed in reverse
character by character, and when (index of the character & 3 == 0), the string "ftc_oc_ip" is printed as well
which we can reverse with some python.

picoCTF{3_digit_hex_GT_999_8a05b9a1}
"""
