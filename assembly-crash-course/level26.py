from pwn import *

context.arch = "amd64"
p = process('/challenge/run')

code = """
cmp  rdi ,3
jg default
mov rax, [rsi + rdi * 8]
jmp rax
default:
        mov rax, [rsi + 32]
        jmp rax
"""

print(p.recvuntil(b'Please give me your assembly in bytes (up to 0x1000 bytes):').decode())
p.recvline()
p.send(asm(code))
print(p.recvall().decode())
