# Intro
This idea came up when I watched Junferno's Bad Apple on Desmos video but I can't make such a complicated project like this so I decided to make something easier.

Finished date: 11/22/2023.

# Guide
- Install OpenCV
```python
pip install opencv-python
```
- Replace the direction of the image that you want to convert
```python
img = cv2.imread('')
```
 
# Code explaination
- Import OpenCV library
```python
import cv2
```
- List of 11 letters correspond to the darkest to the lightest color
```python
ascii_chars = ["B", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]
```
- Read the image, resize the image to the lower resolution, convert to gray image, then create `new_pixels` string that will store the letters later.
```python
img = cv2.imread('')
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
```
- Create text file that will store the converted "image" 
```python
f = open('ascii_art.txt','w')
```
- Access every pixel values in the image in order from left to right, replace each pixel with the letter which corresponds to its brightness (pixels in gray images has the value from 0 to 255. 0 is the darkest and white is the lightest, there is 11 letters so we have to floor divide them to find the letter that matches the pixel brightness), finaly, write all into the text file.   
```python
for x in range(height_n):
    for y in range(width_n):
        pixel = gray_img[x,y]
        pixels = ascii_chars[pixel//25]
        new_pixels.append(pixels)
        
    with open('ascii_art.txt','a') as f:
            f.write(''.join(new_pixels))
            f.write('\n')
    new_pixels = []
```
# Note
- There are only 11 levels of brightness, I recommend using high contrast picture for best result.
- Avoid using very high resolution as well as very detailed images due to the low resolution of the output image.
- If the image is in the same folder of the `main.py` file, you can open the folder with Visual Studio Code and place the name of the image in `img = cv2.imread('')`, otherwise, you have to place the whole direction of this image.
# Some results
![example1](https://github.com/zephiroxz/Ascii_art/blob/main/Result%20images/example1.png)

![example2](https://github.com/zephiroxz/Ascii_art/blob/main/Result%20images/example2.png)

![example3](https://github.com/zephiroxz/Ascii_art/blob/main/Result%20images/example3.png)
# References
[1]  https://www.geeksforgeeks.org/opencv-python-tutorial/

[2]  https://www.w3schools.com/python/python_file_write.asp

