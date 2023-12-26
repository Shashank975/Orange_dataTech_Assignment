from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance

import os


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1560x800+0+0")
        self.root.title("Face_Recogonition_System")

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"D:\College Project\Face-Recognition-Attendence-System\Images_GUI\Blue.png")
        img=img.resize((1560,180),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=-10,width=1560,height=180)

        # backgorund image 
        bg1=Image.open(r"D:\College Project\Face-Recognition-Attendence-System\Images_GUI\bg3.jpg")
        bg1=bg1.resize((1560,800),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=170,width=1560,height=800)


        #title section
        title_lb1 = Label(bg_img,text="<--Attendance Managment System Using Facial Recognition-->",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1560,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"D:\College Project\Face-Recognition-Attendence-System\Images_GUI\std1.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.student_Panels,image=self.std_img1,cursor="hand2")
        std_b1.place(x=350,y=100,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.student_Panels,text="Student Panel",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=350,y=280,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"D:\College Project\Face-Recognition-Attendence-System\Images_GUI\det1.jpg")
        det_img_btn=det_img_btn.resize((180,180),Image.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.face_rec,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=580,y=100,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.face_rec,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=580,y=280,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"D:\College Project\Face-Recognition-Attendence-System\Images_GUI\att.jpg")
        att_img_btn=att_img_btn.resize((180,180),Image.LANCZOS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.attendance_Panel,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=810,y=100,width=180,height=180)

        att_b1_1 = Button(bg_img,command=self.attendance_Panel,text="Attendance",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=810,y=280,width=180,height=45)

        

        # Top 4 buttons end.......
        # ---------------------------------------------------------------------------------------------------------------------------
        # Start below buttons.........
         # Train   button 5
        tra_img_btn=Image.open(r"D:\College Project\Face-Recognition-Attendence-System\Images_GUI\tra1.jpg")
        tra_img_btn=tra_img_btn.resize((180,180),Image.LANCZOS)
        self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img,command=self.train_Panels,image=self.tra_img1,cursor="hand2",)
        tra_b1.place(x=1040,y=100,width=180,height=180)

        tra_b1_1 = Button(bg_img,command=self.train_Panels,text="Data Train",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        tra_b1_1.place(x=1040,y=280,width=180,height=45)

        # Photo   button 6
        pho_img_btn=Image.open(r"D:\College Project\Face-Recognition-Attendence-System\Images_GUI\Gallery-icon.png")
        pho_img_btn=pho_img_btn.resize((180,180),Image.LANCZOS)
        self.pho_img1=ImageTk.PhotoImage(pho_img_btn)

        pho_b1 = Button(bg_img,command=self.open_img,image=self.pho_img1,cursor="hand2",)
        pho_b1.place(x=580,y=380,width=180,height=180)

        pho_b1_1 = Button(bg_img,command=self.open_img,text="Archives",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        pho_b1_1.place(x=580,y=560,width=180,height=45)

        
        

        # exit   button 8
        exi_img_btn=Image.open(r"D:\College Project\Face-Recognition-Attendence-System\Images_GUI\exi.jpg")
        exi_img_btn=exi_img_btn.resize((180,180),Image.LANCZOS)
        self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img,command=self.Close,image=self.exi_img1,cursor="hand2",)
        exi_b1.place(x=810,y=380,width=180,height=180)

        exi_b1_1 = Button(bg_img,command=self.Close,text="Exit",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        exi_b1_1.place(x=810,y=560,width=180,height=45)

# ==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("data_img")
# ==================Functions Buttons=====================
    def student_Panels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_Panels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendance_Panel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def Close(self):
        root.destroy()
    
    





if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
