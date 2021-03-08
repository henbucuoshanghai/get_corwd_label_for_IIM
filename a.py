import json,cv2
with open("./jsons/0078.json",'r') as load_f:
     load_dict = json.load(load_f)
     print(load_dict['boxes'])
img=cv2.imread('./images/0078.jpg')
a=load_dict['boxes']
for i in range(len(a)):
    print(123456789)
    print((a[i][0], a[i][1]), (a[i][2], a[i][3]))

    print(123456789)
    cv2.rectangle(img, (int(a[i][0]), int(a[i][1])), (int(a[i][2]), int(a[i][3])), (0, 255, 0), 2)
cv2.imwrite('gtbbox.jpg',img)

bb=cv2.imread('./images/0078.jpg')
b=load_dict['points']
print(b)
for i in range(len(a)):
    cv2.circle(bb, (int(b[i][0]), int(b[i][1])), 9, (0, 0, 213),-1)
    #cv2.rectangle(img, (int(a[i][0]), int(a[i][1])), (int(a[i][2]), int(a[i][3])), (0, 255, 0), 2)
cv2.imwrite('bb.jpg',bb)
