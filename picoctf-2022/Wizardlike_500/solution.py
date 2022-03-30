from pwn import *

program = ELF("./game")

# Let us walk through walls by overriding the movability check.
program.write(0x1657, b'\x01')

# Give us full vision of the map by overriding what it means to be a wall in the check.
program.write(0x14eb, b'\xff')
program.write(0x142b, b'\xff')

program.save("game_patched")

# picoCTF{ur_4_w1z4rd_8f4b04ae}
