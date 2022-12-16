
f=open("./flag")

flag=f.readline()

f.close()


key="i like cats.. ah? 'i like dogs'?????"

enc=[11, 28, 2, 8, 0, 42, 63, 47, 30, 49, 111, 59, 27, 6, 19, 32, 39, 37, 26, 34, 107, 7, 65, 29, 110, 38, 53, 20, 98]

d=""

for i, e in enumerate(enc):
    d+=chr(e^ord(key[((i**2)//2)%(i+1)]))



print(d)


