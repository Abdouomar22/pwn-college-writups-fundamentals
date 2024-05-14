from pwn import *
from sympy import sympify

p = process("/challenge/embryoio_level100")
challenge_prompt = p.recvuntil(b'compute responses for.\n')
challenge_prompt = p.recvline().decode()
print(challenge_prompt)
challenge_eq = challenge_prompt.split()[-1]

expr = sympify(challenge_eq)
result = expr.evalf()
result = int(result)
print(result)
p.sendline(str(result).encode())
while True :
    challenge_prompt = p.recvline().decode()
    challenge_prompt = p.recvline().decode()
    if challenge_prompt.__contains__('[GOOD]') :
        print(p.recvall().decode())
        break
    print(challenge_prompt)

    challenge_eq = challenge_prompt.split(": ")[-1]
    
    expr = sympify(challenge_eq)

    result = expr.evalf()

    result = int(result)
    
    print(result)
    
    p.sendline(str(result).encode())

print(p.recvall().decode())

