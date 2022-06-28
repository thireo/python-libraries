#!/usr/bin/env python
from PIL import Image, ImageDraw, ImageFont

msg = 'test\nwow'
W,H = (177,118)
img = Image.new('RGBA',(W,H),color = (255,255,255,0))
""" d = ImageDraw.Draw(img)
w, h = d.textsize(msg)
d.text(((W-w)/2,(H-h)/2),msg,fill=(0,0,0))
d.line([(0,0),(0,H-1),(W-1,H-1),(W-1,1),(2,0)],fill=(0,0,0),width=3)
img.save('test.png') """
#img.show()
fnt = ImageFont.truetype(font='C:/Windows/Fonts/times.ttf',size=30)

labels = ['100nF\n0402','10nF\n0402','100uF\n0805','100nF\n0402','10nF\n0402','100uF\n0805','100nF\n0402','10nF\n0402','100uF\n0805','100nF\n0402','10nF\n0402','100uF\n0805','100nF\n0402','10nF\n0402','100uF\n0805','100nF\n0402','10nF\n0402','100uF\n0805','100nF\n0402','10nF\n0402','100uF\n0805','100nF\n0402','10nF\n0402','100uF\n0805','100nF\n0402','10nF\n0402','100uF\n0805','100nF\n0402','10nF\n0402','100uF\n0805','100nF\n0402','10nF\n0402','100uF\n0805','100nF\n0402','10nF\n0402','100uF\n0805','100nF\n0402','10nF\n0402','100uF\n0805','100nF\n0402','10nF\n0402','100uF\n0805','100nF\n0402','10nF\n0402','100uF\n0805','100nF\n0402','10nF\n0402','100uF\n0805','100nF\n0402','10nF\n0402','100uF\n0805','100nF\n0402','10nF\n0402','100uF\n0805',]

greatimg = Image.new('RGBA',(W*18,H*20),color = (255,255,255,0))
""" textc = 0
for x in range(0,19):
    for y in range(0,21):
        if text[textc]:
            img = Image.new('RGBA',(W,H),color = (255,255,255,0))
            msg = text[textc]
            d = ImageDraw.Draw(img)
            w, h = d.textsize(msg,font=fnt)
            d.text((W/2-w/2,H/2-h/2),msg,font=fnt,fill=(0,0,0,255),align='left')
            d.line([(0,0),(0,H-1),(W-1,H-1),(W-1,1),(2,0)],fill=(0,0,0),width=3)
            img.save('test.png')
            img.show()
            greatimg.paste(img,(W*x,H*y))
            textc += 1 """

x = 0
y = 0
for label in labels:
    if x < 19:
        if y < 21:
            img = Image.new('RGBA',(W,H),color = (255,255,255,0))
            d = ImageDraw.Draw(img)
            w, h = d.textsize(label,font=fnt)
            d.text((W/2-w/2,H/2-h/2),label,font=fnt,fill=(0,0,0,255),align='left')
            d.line([(0,0),(0,H-1),(W-1,H-1),(W-1,1),(2,0)],fill=(0,0,0),width=3)
            #img.save('test.png')
            #img.show()
            greatimg.paste(img,(W*x,H*y))
            y += 1
        else:
            x += 1
            y = 0
    else:
        print('Enough labels for you, young man!')


#greatimg.paste(img,(0,0))
#greatimg.paste(img,(0,H))
#greatimg.paste(img,(W,0))
#greatimg.paste(img,(W,H))
greatimg.save('test2.png')
greatimg.show()

#LABELSIZE: 15 x 10 mm
#A4 SIZE: 210 x 297 mm
#A4 RES 300dpi: 2480 x 3508 pixels