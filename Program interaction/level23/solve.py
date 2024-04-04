from pwn import * 

binary = '/challenge/embryoio_level23'

p = process(binary)

p.sendline('ofnkaxnz')

output = p.recvall()

print(output)
