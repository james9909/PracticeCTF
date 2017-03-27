def group(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]

enc = "8a7fca9234d2f19c8abfcd812971a26c8c510dcaefd5061b191ad41d8b57d0ce631f5074f94b32730d0c025f1d7aacd7be1ab1632e4285edc3733b142935c60b90383bad42309f7f6850d2b4250a713d0b2d7a97350465a02554d29d92bfefafd64ddd0de1b187cd670783f5e28d681dd401ed3009d05ce4ef600d364a2c953e4cc801b880dddef59829a5ad08bd8a6373d559bc117f816333174e918d0587de5cca214701dbe9f7f42da7bccf074b811292b9d4dc398866ef95869b22b3941e78635bc95eaa7662a2ddf3e3d45cf1084f4233d6c396e8a0e6fbf597d07b88178d03f3f7757bdbdaaed60729d08bb180b42dad5453b2128a32f6612b13ea5d9fef843bee79633652a6d6ae08e964609f00e883ab809346226dff6887080fb68b"

dec = ""
for chunk in group(enc, 32):
    print chunk

# Looking at the source we find that the hash function takes the md5 hash of every 4 characters
# in the string and contatenates all the hashes together. This means that we just need to look up
# every 32 characters in lookup table, which should be feasible because it's the hash of a 4 character string.
# I used https://www.hashkiller.co.uk/md5-decrypter.aspx

# The password is OMG_it_took_like_LITerally_s0oO00_long_2_MAK3_md5_werrk_you_have_no_id34

# Plugging that into the password field gives you the flag:
# easyctf{OUR_3nCRYpti0n_is_N0T_br0k3n_Ur_brok3n_6c5a390d}
