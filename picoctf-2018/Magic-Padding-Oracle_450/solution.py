from pwn import *
from paddingoracle import PaddingOracle, BadPaddingException
import time

class PadBuster(PaddingOracle):
    def oracle(self, data):
        try:
            r = remote("2018shell3.picoctf.com", 4966, level="error")
            r.recvuntil("What is your cookie?")
            r.sendline(str(data).encode("hex"))

            resp = r.recvall()
            r.close()
            if "invalid padding" in resp:
                raise BadPaddingException
            print("Found byte")
        except (EOFError, pwnlib.exception.PwnlibException):
            time.sleep(0.1)
            self.oracle(data)

sample_cookie = "5468697320697320616e2049563435366bfb3fae87ed7fa62690594a892409e6a4245eb2a5ff17ced3f0daf18f0cb05aaa9a2c4f43ade989de937a8439a7a9ea7f7ee59558d62d81db804a3b8ce1c5574dfdacead33f1fdf0580901129a2ec56".decode("hex")
desired = '{"username": "guest", "expires": "2100-01-07", "is_admin": "true"}'
iv = sample_cookie[:16]

padbuster = PadBuster()
encrypted = padbuster.encrypt(desired, block_size=16, iv=iv)
print(str(encrypted).encode("hex"))

"""
What is your cookie?
99ac809501c57355e3d02c638e91a1dae630d949dab0eaba57dc4b68dd545835041338f8189122f95aafdf75c0ff553b9e84adf9d0c3faea900e662e26c42719c49b1c5d7a1f6759d353978299460ea4a3fbd66b79b2bd839b58df85fb321e635468697320697320616e204956343536
username: guest
Admin? true
Cookie is not expired
The flag is: picoCTF{0r4cl3s_c4n_l34k_6412acff}
"""
