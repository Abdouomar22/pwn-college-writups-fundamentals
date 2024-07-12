from pwn import *

context.arch = "amd64"
p = process('/challenge/run')

code = """
mov rbx ,0
mov rsi , 0
cmp rdi , 0
jne loop_start
mov rax , 0
jmp end
loop_start:
	mov sil , byte ptr [rdi +rbx]
    cmp rsi , 0
	je end
	inc rax
	inc rbx
	jmp loop_start
end:
	nop
"""

print(p.recvuntil(b'Please give me your assembly in bytes (up to 0x1000 bytes):').decode())
p.recvline()
p.send(asm(code))
print(p.recvall().decode())
