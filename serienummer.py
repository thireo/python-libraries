from tkinter import *
from PIL import Image, ImageDraw, ImageFont, ImageTk


def save_2_file(event):
    print('')

fnt = ImageFont.truetype(font='C:/Windows/Fonts/Arial.ttf',size=64)

master = Tk()
master.title('S/N ENGRAVER 2020')
master.configure(background='black')
#master.geometry('256x512')



bgck = 'dim gray'

lbl1 = Label(master, text="S/N start:")
lbl1.grid(row=0,sticky=W)
lbl1.config(background='black',foreground='white')

e1 = Entry(master)
e1.config(background=bgck,foreground='white')
e1.focus()
e1.grid(row=0, column=1,sticky=W)



#textbox = Text(master,height=25,width=35)
#textbox.grid(row=5,columnspan=3)
#textbox.config(background=bgck,foreground='white')

#imgFile = PhotoImage(file='test.png')
#imgLabel = Label(master)#,image=imgFile)
#imgLabel.grid(row=0,rowspan=3,columnspan=2,column=2,pady=5)

def quitty_mcquitface(_event=None):
    master.quit()

def save_entries(_event=None):
    #textbox.insert(END,'%s\n'%(e1.get()))
    global lines 
    lines = str('%s'%(e1.get()))
    display_preview()

def display_preview():
    '''W,H = (177,118)
    imageFile = Image.new('RGBA',(W,H),color = (255,255,255,0))
    d = ImageDraw.Draw(imageFile)
    w, h = d.textsize(lines,font=fnt)
    d.text((W/2-w/2,H/2-h/2),lines,font=fnt,fill=(0,0,0,255),align='center')
    #d.line([(0,0),(0,H-1),(W-1,H-1),(W-1,1),(2,0)],fill=(0,0,0),width=3)
    imageFile.save('test.png')
    global imgtk
    imgtk = ImageTk.PhotoImage(Image.open('test.png'))
    imgLabel.config(image=imgtk)'''
    #imgLabel.after(500,display_preview)


allTheLabels = []


def save_lines(_event=None):
    lines = str('%s'%(e1.get()))
    if lines !='':
        sn = int(lines)
        for i in range(20):
            allTheLabels.append(str(sn+i))
        #allTheLabels.append(lines)
        print(allTheLabels)
        #textbox.insert(END,lines+'\n')
        e1.delete(0,END)
        e1.focus()
        generate_print()
    
def generate_print(_event=None):
    W,H = (1000,750)
    greatimg = Image.new('RGBA',(W*7,H*5),color = (255,255,255,0))
    #greatDrawing = ImageDraw.Draw(greatimg)
    #greatDrawing.line([(0,0),(0,(H*7)-1),((W*6)-1,(H*7)-1),((W*6)-1,1),(2,0)],fill=(255,255,255),width=3)
    x = 0
    y = 0
    for label in allTheLabels:
        
        if x < 6:
            if y < 4:
                print("%d/%d - %s"%(x,y,label))
                img = Image.new('RGBA',(W,H),color = (0,0,0,0))
                d = ImageDraw.Draw(img)
                w, h = d.textsize(label,font=fnt)
                d.text((W/2-w/2,H/2-h/2),label,font=fnt,fill=(0,0,0,255),align='center')
                d.line([(0,0),(0,H-1),(W-1,H-1),(W-1,1),(2,0)],fill=(0,0,0),width=3)
                #img.save('test.png')
                #img.show()
                greatimg.paste(img,(W*x,H*y))
                y += 1
            else:
                x += 1
                y = 0
                print("%d/%d - %s"%(x,y,label))
                img = Image.new('RGBA',(W,H),color = (0,0,0,0))
                d = ImageDraw.Draw(img)
                w, h = d.textsize(label,font=fnt)
                d.text((W/2-w/2,H/2-h/2),label,font=fnt,fill=(0,0,0,255),align='center')
                d.line([(0,0),(0,H-1),(W-1,H-1),(W-1,1),(2,0)],fill=(0,0,0),width=3)
                #img.save('test.png')
                #img.show()
                greatimg.paste(img,(W*x,H*y))
                y += 1
        else:
            print('Enough labels for you, young man!')
    greatimg.save('serienumre.png')
    greatimg.show()

cancelBtn = Button(master,text='QUIT',command=master.quit)
cancelBtn.grid(row=4,column=0,sticky=W,pady=5)
cancelBtn.config(background=bgck,foreground='white')

'''saveBtn = Button(master,text='PREVIEW LABEL',command=save_entries)
saveBtn.grid(row=4,column=1,sticky=W,pady=5)
saveBtn.config(background=bgck,foreground='white')'''

saveFileBtn = Button(master,text='Generate',command=save_lines)
saveFileBtn.grid(row=0,column=3,sticky=E,pady=5)
saveFileBtn.config(background=bgck,foreground='white')

master.bind('<Return>', save_entries)
master.bind('<Control-s>', save_lines)
master.bind('<Escape>',quitty_mcquitface)
save_entries()
lines = 'PREVIEW'
display_preview()
mainloop( )