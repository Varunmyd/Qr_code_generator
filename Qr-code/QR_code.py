from tkinter import *
import pyqrcode
from PIL import ImageTk,Image
root=Tk()
def fntn():
    name=entry_name.get()
    link=entry_link.get()
    file_name=name + '.png'
    url=pyqrcode.create(link)
    url.png(file_name,scale=8)
    image=ImageTk.PhotoImage(Image.open(file_name))
    label=Label(image=image)
    label.image=image
    canvas.create_window(200,400,window=label)




canvas=Canvas(root,width=400,height=600)
canvas.pack()
app_label=Label(text='QR Code_Generator',fg='blue',font=('Arial',30))
canvas.create_window(200,30,window=app_label)
name_label=Label(root,text='Link Name')
link_label=Label(root,text='Link')
canvas.create_window(200,80,window=name_label)
canvas.create_window(200,130,window=link_label)
entry_name=Entry(root)
entry_link=Entry(root)
canvas.create_window(200,100,window=entry_name)
canvas.create_window(200,150,window=entry_link)
button=Button(root,text='QR Code Generator',fg='white',bg='red',command=fntn)
canvas.create_window(200,190,window=button)




root.mainloop()