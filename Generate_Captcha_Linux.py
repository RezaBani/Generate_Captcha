#!/usr/bin/python3
from PIL import ImageFont, ImageDraw, Image
import string
import random
import numpy as np
import cv2 

def generate_picture():
    size = random.randint(10,16)
    length = random.randint(5,8)
    captcha_text = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    
    img = np.zeros(shape=(60, 120, 3), dtype=np.uint8)
    x_pt1 = random.choice(range(int(img.shape[1]/3)))
    x_pt2 = random.choice(range(int(2*img.shape[1]/3),img.shape[1]))
    y_pt1 = random.choice(range(int(img.shape[0])))
    if y_pt1 > (2*img.shape[0]/3):
        y_pt2 = random.choice(range(int(img.shape[0]/3)))
    elif y_pt1 > (img.shape[0]/3) and y_pt1 < (2*img.shape[0]/3):
        y_pt2 = random.choice(range((int(img.shape[0]/3)),int(2*img.shape[0]/3)))
    elif y_pt1 < (img.shape[0]/3):
        y_pt2 = random.choice(range(int(2*img.shape[0]/3),img.shape[0]))
    img_pil = Image.fromarray(img)
    
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype(font='/usr/local/share/fonts/v/Vazir_Bold.ttf', size=30)
    
    draw.text((5,10), captcha_text, font=font, fill=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    draw.line([(x_pt1,y_pt1),(x_pt2,y_pt2)], width=4, fill=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    
    img = np.array(img_pil)

    thresh = 0.05
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            rdn = random.random()
            if rdn < thresh:
                img[i][j] = 0
            elif rdn > 1-thresh:
                img[i][j] = 250

    # img_blurred = cv2.blur(img,(2,2))
    cv2.imwrite('/home/reza/Downloads/image.jpg', img)
    
if __name__=="__main__":
    generate_picture()