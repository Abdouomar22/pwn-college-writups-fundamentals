from pwn import *

context.arch = "amd64"
p = process('/challenge/run')

code = """
mov rax , 0
mov rcx , 0
cmp rdi , 0
je return
mov rsi , rdi

loop_start :
	cmp byte ptr [rsi] , 0
	je return
	cmp byte ptr [rsi] , 0x5a
	jnle else
	mov rbx , 0x403000
	mov rdi , [rsi]
	call rbx
	mov [rsi] , rax
	inc rcx
	jmp loop_start
	else :
		inc rsi
		jmp loop_start

return:
	mov rax , rcx
	ret
"""

print(p.recvuntil(b'Please give me your assembly in bytes (up to 0x1000 bytes):').decode())
p.recvline()
p.send(asm(code))
print(p.recvall().decode())
