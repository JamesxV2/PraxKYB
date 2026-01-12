#!/bin/python

from pwn import *

p = process("/challenge/run")

p.recvuntil(b"e = 0x")
e = int(p.recvline().strip().decode(), 16)

p.recvuntil(b"p = 0x")
p = int(p.recvline().strip().decode(), 16)

p.recvuntil(b"q = 0x")
q = int(p.recvline().strip().decode(), 16)

p.recvuntil(b"Flag Ciphertext (hex): ")
flag = int(p.recvline().strip().decode(), 16)

pt = pow(flag, e, p*q)

print(pt)
