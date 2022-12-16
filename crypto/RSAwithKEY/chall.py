from Crypto.Util.number import *

f = open("./flag")
flag=f.readline()
f.close()

flag = bytes_to_long(flag.encode("utf-8"))

e = 65537

p = getPrime(1024)
q = getPrime(1024)
n = p * q

c = pow(flag, e, n)

print(f"e: {e}")
print(f"p: {p}")
print(f"q: {q}")
print(f"c: {c}")