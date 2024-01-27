from cProfile import label
import importlib
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
import subprocess
from student import Student
from train import Train
from face_recognition import Face_recognition



class Face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #first image
        img=Image.open("collage_images/Unknown-2.jpeg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


        #Second image
        img1=Image.open("collage_images/Unknown-3.jpeg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=550,height=130)

        #Third image
        img2=Image.open("collage_images/Unknown.jpeg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)


        # Background image
        img3=Image.open("collage_images/premium_photo-1661898424988-a5f6d40d3db2.webp")
        img3=img3.resize((1500,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # Student button
        img4=Image.open("collage_images/photo-1671726203454-5d7a5370a9f4.webp")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"), bg="white",fg="blue")
        b1_1.place(x=200,y=300,width=220,height=40)

        # Face Detector button
        img5=Image.open("collage_images/umer.jpeg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"), bg="white",fg="blue")
        b1_1.place(x=500,y=300,width=220,height=40)

        # Attendance  button
        img6=Image.open("collage_images/Unknown-4.jpeg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"), bg="white",fg="blue")
        b1_1.place(x=800,y=300,width=220,height=40)

        # Help Desk button
        img7=Image.open("collage_images/photo-1528901166007-3784c7dd3653.webp")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"), bg="white",fg="blue")
        b1_1.place(x=1100,y=300,width=220,height=40)

        # Train Data  button
        img8=Image.open("collage_images/photo-1594729095022-e2f6d2eece9c.webp")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"), bg="white",fg="blue")
        b1_1.place(x=200,y=580,width=220,height=40)

         # Photos  button
        img9=Image.open("collage_images/elon_2.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"), bg="white",fg="blue")
        b1_1.place(x=500,y=580,width=220,height=40)

         # Developer  button
        img10=Image.open("collage_images/Unknown-9.jpeg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"), bg="white",fg="blue")
        b1_1.place(x=800,y=580,width=220,height=40)

         # Exit  button
        img11=Image.open("collage_images/Unknown-1.jpeg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"), bg="white",fg="blue")
        b1_1.place(x=1100,y=580,width=220,height=40)

    
    def open_img(self):
        file="/Users/umerkhayammir/Desktop/Face_Recognition system/data"
        subprocess.run(['open', file])
        # here i used "subprocees.run(['open',file])" in place of os.startfile("data") of os library because in macbook os.startfile(" ") can't support
        # so here we import subprocess and then use the function subprocess.run(["open",file])



       # """""""""""""""FUNCTION BUTTON"""""""""
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Train(self.new_window)

    def face_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Face_recognition(self.new_window)



if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition_system(root)
    root.mainloop()