f=open("./flag")
flag=f.readline()
f.close()


key="i like cats.. ah? 'i like dogs'?????"

enc=[];


for i, f in enumerate(flag):
    enc.append(ord(f)^ord(key[((i**2)//2)%(i+1)]))

print(enc)


