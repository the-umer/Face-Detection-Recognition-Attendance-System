from ast import Delete, Pass
from cProfile import label
from cgitb import text
from distutils import command
from logging import root
from multiprocessing import connection
from optparse import Values
import sqlite3
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")




        #""""""""VARIABLES"""""""
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()



        #first image
        img=Image.open("/Users/umerkhayammir/Desktop/Face_Recognition system/collage_images/Unknown-11.jpeg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


        #Second image
        img1=Image.open("/Users/umerkhayammir/Desktop/Face_Recognition system/collage_images/Unknown-12.jpeg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=550,height=130)

        #Third image
        img2=Image.open("/Users/umerkhayammir/Desktop/Face_Recognition system/collage_images/Unknown-13.jpeg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)


        # Background image
        img3=Image.open("/Users/umerkhayammir/Desktop/Face_Recognition system/collage_images/premium_photo-1661898424988-a5f6d40d3db2.webp")
        img3=img3.resize((1500,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=25,y=50,width=1400,height=610)


        # LEFT LABEL FRAME
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=680,height=560)


        img_left=Image.open("/Users/umerkhayammir/Desktop/Face_Recognition system/collage_images/Unknown-16.jpeg")
        img_left=img_left.resize((660,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=660,height=130)


        # current course
        Current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        Current_course_frame.place(x=10,y=135,width=680,height=150)


        #department label
        dep_label=Label(Current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        #combo box
        dep_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        #Course label
        course_label=Label(Current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        #combo box
        course_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #Year label
        year_label=Label(Current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

          #combo box
        dep_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #Semester label
        Semester_label=Label(Current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        Semester_label.grid(row=1,column=2,padx=10,sticky=W)


          #combo box
        dep_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Semester","Semestr-1","Semester-2",)
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        # Class Student information
        Class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student information",font=("times new roman",12,"bold"))
        Class_student_frame.place(x=10,y=250,width=680,height=400)


        #STUDENT ID label
        StudentID_label=Label(Class_student_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        StudentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        #Entry field
        studentID_entry=ttk.Entry(Class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


         #STUDENT NAME label
        StudentName_label=Label(Class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        StudentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        #Entry field
        studentName_entry=ttk.Entry(Class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


         #CLASS DIVISION label
        class_div_label=Label(Class_student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        #Entry field
        # class_div_entry=ttk.Entry(Class_student_frame,width=20,font=("times new roman",12,"bold"))
        # class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        div_combo=ttk.Combobox(Class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=18)
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        #ROLL NUMBER label
        roll_number_label=Label(Class_student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        roll_number_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        #Entry field
        class_div_entry=ttk.Entry(Class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        class_div_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


         #GENDER label
        gender_number_label=Label(Class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_number_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        # #Entry field
        # gender_entry=ttk.Entry(Class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        # gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        gender_combo=ttk.Combobox(Class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)


         #DATE OF BIRTH(DOB) label
        dob_label=Label(Class_student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        #Entry field
        class_div_entry=ttk.Entry(Class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        class_div_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        #EMAIL label
        email_label=Label(Class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        #Entry field
        class_div_entry=ttk.Entry(Class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        class_div_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        #PHONE NUMBER label
        phone_label=Label(Class_student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        #Entry field
        phone_entry=ttk.Entry(Class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        #ADDRESS label
        adress_label=Label(Class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        adress_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        #Entry field
        phone_entry=ttk.Entry(Class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


        #TEACHER NAME label
        teacher_label=Label(Class_student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        #Entry field
        teacher_entry=ttk.Entry(Class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)


        # RADIO BUTTONS
        self.var_radio1=StringVar()
        radiobutton1=ttk.Radiobutton(Class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobutton1.grid(row=6,column=0)

        radiobutton2=ttk.Radiobutton(Class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobutton2.grid(row=6,column=1)

        # BUTTON FRAME
        button_frame=Frame(Class_student_frame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=0,y=200,width=675,height=35)


        save_button=Button(button_frame,text="Save",command=self.add_data,width=18,font=("times new roman",13,"bold"),bg="white",fg="blue")
        save_button.grid(row=0,column=0)

        update_button=Button(button_frame,text="Update",command=self.update_data,width=18,font=("times new roman",13,"bold"),bg="white",fg="blue")
        update_button.grid(row=0,column=1)

        delete_button=Button(button_frame,text="Delete",command=self.delete_data,width=18,font=("times new roman",13,"bold"),bg="white",fg="blue")
        delete_button.grid(row=0,column=2)

        reset_button=Button(button_frame,text="Reset",command=self.reset_data,width=18,font=("times new roman",13,"bold"),bg="white",fg="blue")
        reset_button.grid(row=0,column=3)
        
        # BUTTON FRAME 2
        button_frame1=Frame(Class_student_frame,bd=2,relief=RIDGE,bg="white")
        button_frame1.place(x=0,y=230,width=675,height=35)

        take_photo_button=Button(button_frame1,command=self.generate_dataset,text="Take Photo sample",width=40,font=("times new roman",13,"bold"),bg="white",fg="blue")
        take_photo_button.grid(row=0,column=0)

        update_photo_button=Button(button_frame1,text="Update Photo Sample",width=40,font=("times new roman",13,"bold"),bg="white",fg="blue")
        update_photo_button.grid(row=0,column=1)






        # RIGHT LABEL FRAME
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=700,y=10,width=680,height=580)

        img_right=Image.open("/Users/umerkhayammir/Desktop/Face_Recognition system/collage_images/Unknown-14.jpeg")
        img_right=img_right.resize((660,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=660,height=130)


        # """"""""""SEARCH SYSTEM"""""""""
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=10,y=130,width=670,height=75)

        search_label=Label(Search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="red",fg='white')
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Entry field
        search_entry=ttk.Entry(Search_frame,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_button=Button(Search_frame,text="Search",width=14,font=("times new roman",13,"bold"),bg="white",fg="blue")
        search_button.grid(row=0,column=3,padx=4)

        showAll_button=Button(Search_frame,text="Show All",width=14,font=("times new roman",13,"bold"),bg="white",fg="blue")
        showAll_button.grid(row=0,column=4,padx=4)


        #"""""""""""""""TABLE FRAME"""""""""
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=210,width=670,height=350)


        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","dob","email","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
        

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        
        #"""""""""""""""FUNCTION DECLARATION"""""""""""
        # ADD data to the Database

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
          messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="Umer@123", database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                            self.var_dep.get(),
                                                                                            self.var_course.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_semester.get(),
                                                                                            self.var_std_id.get(),
                                                                                            self.var_std_name.get(),
                                                                                            self.var_div.get(),
                                                                                            self.var_roll.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_phone.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_teacher.get(),
                                                                                            self.var_radio1.get()

                                                                                          ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    # """""""""""FETCH DATA""""""""""
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="Umer@123", database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
                conn.commit()
        conn.close()

    # """"""""""GET CURSOR"""""""""
    def get_cursor(self,event=""):
      cursor_focus=self.student_table.focus()
      content=self.student_table.item(cursor_focus)
      data=content["values"]

      self.var_dep.set(data[0]),
      self.var_course.set(data[1]),
      self.var_year.set(data[2]),
      self.var_semester.set(data[3]),
      self.var_std_id.set(data[4]),
      self.var_std_name.set(data[5]),
      self.var_div.set(data[6]),
      self.var_roll.set(data[7]),
      self.var_gender.set(data[8]),
      self.var_dob.set(data[9]),
      self.var_email.set(data[10]),
      self.var_phone.set(data[11]),
      self.var_address.set(data[12]),
      self.var_teacher.set(data[13]),
      self.var_radio1.set(data[14])



#""""""""""""" UPDATE FUNCTION """"""""""
    def update_data(self):
      if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
         messagebox.showerror("Error","All Fields are required",parent=self.root)
      else:
          try:
              update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
              if update>0:
                conn=mysql.connector.connect(host="localhost", username="root", password="Umer@123", database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                          self.var_dep.get(),
                                                                                                                                                                          self.var_course.get(),
                                                                                                                                                                          self.var_year.get(),
                                                                                                                                                                          self.var_semester.get(),
                                                                                                                                                                          self.var_std_name.get(),
                                                                                                                                                                          self.var_div.get(),
                                                                                                                                                                          self.var_roll.get(),
                                                                                                                                                                          self.var_gender.get(),
                                                                                                                                                                          self.var_dob.get(),
                                                                                                                                                                          self.var_email.get(),
                                                                                                                                                                          self.var_phone.get(),
                                                                                                                                                                          self.var_address.get(),
                                                                                                                                                                          self.var_teacher.get(),
                                                                                                                                                                          self.var_radio1.get(),
                                                                                                                                                                          self.var_std_id.get()
                                                                                                                                                                           ))
              else:
                if not update:
                    return
              conn.commit()
              self.fetch_data()
              conn.close()

              messagebox.showinfo("Sucess","Student details successfully update completed",parent=self.root)
          except Exception as es:
              messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

# """"""""""""""""""""""' DELETE FUNCTION"""""""""""""""
    def delete_data(self):
      if self.var_std_id.get()=="":
        messagebox.showerror("Error","Studenet id must be required",parent=self.root)
      else:
        try:
          delete=messagebox.askyesno("Studenet Delete Page","Do you want to delete this student",parent=self.root)
          if delete>0:
              conn=mysql.connector.connect(host="localhost", username="root", password="Umer@123", database="face_recognizer")
              my_cursor=conn.cursor()
              sql="DELETE FROM student where Student_id =%s"
              val=(self.var_std_id.get())
              my_cursor.execute(sql,(val,))
          else:
            if not delete:
              return

          conn.commit()
          self.fetch_data()
          conn.close()

          messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
        except Exception as es:
              messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


  # """"""""""""""""" RESET FUNCTION  """""""""""""""""
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")




        #"""""""""""""""" GENERATE DATA SET OR TAKE PHOTO SAMPLES """"""""""""""""
    def generate_dataset(self):
      if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
         messagebox.showerror("Error","All Fields are required",parent=self.root)
      else:
          try:
                conn=mysql.connector.connect(host="localhost", username="root", password="Umer@123", database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                  id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                          self.var_dep.get(),
                                                                                                                                                                          self.var_course.get(),
                                                                                                                                                                          self.var_year.get(),
                                                                                                                                                                          self.var_semester.get(),
                                                                                                                                                                          self.var_std_name.get(),
                                                                                                                                                                          self.var_div.get(),
                                                                                                                                                                          self.var_roll.get(),
                                                                                                                                                                          self.var_gender.get(),
                                                                                                                                                                          self.var_dob.get(),
                                                                                                                                                                          self.var_email.get(),
                                                                                                                                                                          self.var_phone.get(),
                                                                                                                                                                          self.var_address.get(),
                                                                                                                                                                          self.var_teacher.get(),
                                                                                                                                                                          self.var_radio1.get(),
                                                                                                                                                                          self.var_std_id.get()==id+1
                                                                                                                                                                           ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
          # except Exception as e: 
          #       messagebox.showerror("Error", str(e), parent=self.root)



    # ===========LOAD PREDEFINED DATA ON FACE FRONTALS FROM OPENCV=============
                face_classsifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                  gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                  faces=face_classsifier.detectMultiScale(gray,1.3,5)
                  # scaling factor=1.3
                  # Minimum Neighbor=5
                  for(x,y,w,h) in faces:
                    face_cropped=img[y:y+h,x:x+w]
                    return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                  ret,my_frame=cap.read()
                  if face_cropped(my_frame) is not None:
                    img_id+=1
                    face=cv2.resize(face_cropped(my_frame),(450,450))
                    face=cv2.cvtColor(face,cv2.COLOR_BGR2BGRA)
                    file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path,face)
                    cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                    cv2.imshow("Cropped Face",face)

                  if cv2.waitKey(1)==13 or int(img_id)==100:
                    break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed")
          except Exception as es:
              messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                      





if __name__ == "__main__":
  root=Tk()
  obj=Student(root)
  root.mainloop()