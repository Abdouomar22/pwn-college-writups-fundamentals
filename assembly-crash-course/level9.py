from pwn import *

context.arch = "amd64"
p = process('/challenge/run')

code = """
    mov rax, rdi
    shr rax, 32
    mov rbx , rax
    mov rax ,0
    mov al , bl

"""

print(p.recvuntil(b'Please give me your assembly in bytes (up to 0x1000 bytes):').decode())
p.send(asm(code))
print(p.recvall().decode())
