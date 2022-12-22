import cv2

a = cv2.imread('./a.png')
c = cv2.imread('./c.png')
flag = cv2.imread('./flag.png')

xored=cv2.bitwise_xor(cv2.bitwise_xor(a,flag),c)

cv2.imwrite("./b.png",xored)
