import cv2

ascii_chars = ["B", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]
img = cv2.imread('example2.jpg')

shape = img.shape
height = shape[0]
width = shape[1]
ratio = height/width
width_n = 500
height_n = int(width_n*ratio*0.55)
dim = (width_n, height_n)
img_n = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
gray_img = cv2.cvtColor(img_n, cv2.COLOR_BGR2GRAY)
new_pixels = []

f = open('ascii_art.txt','w')
    

for x in range(height_n):
    for y in range(width_n):
        pixel = gray_img[x,y]
        pixels = ascii_chars[pixel//25]
        new_pixels.append(pixels)
        
    with open('ascii_art.txt','a') as f:
            f.write(''.join(new_pixels))
            f.write('\n')
    new_pixels = []




