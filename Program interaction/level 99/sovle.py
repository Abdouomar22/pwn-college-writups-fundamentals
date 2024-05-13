from pwn import *

p = process("/challenge/embryoio_level99")

challenge_prompt = p.recvuntil(b'compute responses for.\n')
challenge_prompt = p.recvline().decode()
print(challenge_prompt)
challenge_number = challenge_prompt.split()[-1]

p.sendline(challenge_number.encode())

print(p.recvall().decode())

