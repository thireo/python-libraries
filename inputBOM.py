from tkinter import *
from PIL import Image, ImageDraw, ImageFont, ImageTk


def save_2_file(event):
    print('')

fnt = ImageFont.truetype(font='C:/Windows/Fonts/times.ttf',size=25)

master = Tk()
master.title('SMD LABELER 1000')
master.configure(background='black')
master.geometry('375x615')



bgck = 'dim gray'

lbl1 = Label(master, text="Line 1:")
lbl1.grid(row=0,sticky=W)
lbl2 = Label(master, text="Line 2:")
lbl2.grid(row=1,sticky=W)
lbl3 = Label(master, text="Line 3:")
lbl3.grid(row=2,sticky=W)

lbl1.config(background='black',foreground='white')
lbl2.config(background='black',foreground='white')
lbl3.config(background='black',foreground='white')

e1 = Entry(master)
e1.config(background=bgck,foreground='white')
e1.focus()
e2 = Entry(master)
e2.config(background=bgck,foreground='white')
e3 = Entry(master)
e3.config(background=bgck,foreground='white')

e1.grid(row=0, column=1,sticky=W)
e2.grid(row=1, column=1,sticky=W)
e3.grid(row=2, column=1,sticky=W)



textbox = Text(master,height=25,width=35)
textbox.grid(row=5,columnspan=4)
textbox.config(background=bgck,foreground='white')

imgLabel = Label(master)
imgLabel.grid(row=0,rowspan=3,columnspan=2,column=2,pady=5)



def save_entries(_event=None):
    #textbox.insert(END,'%s\n'%(e1.get()))
    global lines 
    lines = str('%s\n%s\n%s'%(e1.get(),e2.get(),e3.get()))
    display_preview()

def display_preview():
    W,H = (177,118)
    imageFile = Image.new('RGBA',(W,H),color = (255,255,255,0))
    d = ImageDraw.Draw(imageFile)
    w, h = d.textsize(lines,font=fnt)
    d.text((W/2-w/2,H/2-h/2),lines,font=fnt,fill=(0,0,0,255),align='center')
    d.line([(0,0),(0,H-1),(W-1,H-1),(W-1,1),(2,0)],fill=(0,0,0),width=3)
    imageFile.save('preview.png')
    global imgtk
    imgtk = ImageTk.PhotoImage(Image.open('preview.png'))
    imgLabel.config(image=imgtk)
    #imgLabel.after(500,display_preview)


allTheLabels = []
def save_lines(_event=None):
    lines = str('%s\n%s\n%s'%(e1.get(),e2.get(),e3.get()))
    if lines !='\n\n':
        allTheLabels.append(lines)
        print(allTheLabels)
        textbox.insert(END,lines+'\n')
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e1.focus()
        #generate_print()
    
def generate_print(_event=None):
    W,H = (177,118)
    greatimg = Image.new('RGBA',(W*18,H*20),color = (255,255,255,0))
    x = 0
    y = 0
    for label in allTheLabels:
        if x < 19:
            if y < 21:
                img = Image.new('RGBA',(W,H),color = (255,255,255,0))
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
        else:
            print('Enough labels for you, young man!')
    greatimg.save('allTheLabels.png')
    greatimg.show()

cancelBtn = Button(master,text='QUIT',command=master.quit)
cancelBtn.grid(row=6,column=0,columnspan=5,pady=5)
cancelBtn.config(background=bgck,foreground='white')

saveBtn = Button(master,text='PREVIEW',command=save_entries)
saveBtn.grid(row=4,column=0,sticky=W,pady=5)
saveBtn.config(background=bgck,foreground='white')

saveLinesBtn = Button(master,text='ADD LABEL',command=save_lines)
saveLinesBtn.grid(row=4,column=1,sticky=E,pady=5)
saveLinesBtn.config(background=bgck,foreground='white')


saveFileBtn = Button(master,text='GENERATE PRINT',command=generate_print)
saveFileBtn.grid(row=4,column=3,pady=5)
saveFileBtn.config(background=bgck,foreground='white')

master.bind('<Return>', save_entries)
master.bind('<Control-s>', save_lines)
master.bind('<Control-p>', generate_print)
save_entries()
lines = 'PREVIEW'
display_preview()
mainloop( )