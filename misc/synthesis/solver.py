import cv2

a = cv2.imread('./a.png')
b = cv2.imread('./b.png')
c = cv2.imread('./c.png')

xored=cv2.bitwise_xor(cv2.bitwise_xor(a,b),c)

cv2.imwrite("flag.png",xored)

