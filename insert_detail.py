#import dbconnect as db
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from PIL import Image
from PIL import ImageTk
import cv2

def saveDb():
    tx=user.get()
    

def opImage():
    fileName=filedialog.askopenfilename(filetypes=(("*",".jpg"),("*",".png")))
    img = ImageTk.PhotoImage(Image.open(fileName))
    t=Tk()
    
    i=Label(t,image=img)
    i.image=img
    i.place(x=150,y=250)
       

def takephoto():
    cam=cv2.VideoCapture(0)  #to open camera
    cv2.namedWindow("take photo") #to set the title for window
    img_counter=0
    while True:
        ret,frame=cam.read() #to read an image
        cv2.imshow("test",frame)
        if not ret:
            break
        k=cv2.waitKey(1)
        if k%256==27: #for esc key
            break
        elif k%256==32: # for spaced
            img_name="temp.png".format(img_counter)
            cv2.imwrite(img_name,frame)
            img_counter+=1
            print("Image Saved")
            break;
        
    cam.release()
    cv2.destroyAllWindows()
            

    

window=Tk()
user = StringVar()
i = Label(window)
window.title("Insert Person Details")
window.geometry("600x700")
window.resizable(0,0)

f=Frame(window,bg="gray")
f.pack(fill=BOTH,expand=1)

l1=Label(f,text="Registration Form",width=20,font=("bold",15))
l1.place(x=150,y=80)

luname=Label(f,text="Enter User Name",width=20,font=("bold",10)).place(x=100,y=130)#.grid(row=0,column=0)
userName=Entry(f,textvariable=user,width=25).place(x=300,y=130)

b1=Button(f,command=opImage,text="Select Image",width=20).place(x=100,y=170)
b2=Button(f,command=takephoto,text="Take Picture",width=20).place(x=300,y=170)       

b3=Button(f,command=saveDb,text="Insert",width=40).place(x=130,y=200)
window.mainloop()
