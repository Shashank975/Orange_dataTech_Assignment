# import re
# from sys import path
# from tkinter import*
# from tkinter import ttk
# from PIL import Image,ImageTk
# import os
# import mysql.connector
# import cv2
# import numpy as np
# from tkinter import messagebox
# from time import strftime
# from datetime import datetime
# class Face_Recognition:

#     def __init__(self,root):
#         self.root=root
#         self.root.geometry("1540x768+0+0")
#         self.root.title("Face Recognition Panel")

#         # This part is image labels setting start 
#         # first header image  
#         img=Image.open(r"D:\College Project\Face-Recognition-Attendence-System\Images_GUI\banner.jpg")
#         img=img.resize((1540,130),Image.LANCZOS)
#         self.photoimg=ImageTk.PhotoImage(img)

#         # set image as lable
#         f_lb1 = Label(self.root,image=self.photoimg)
#         f_lb1.place(x=0,y=0,width=1540,height=130)

#         # backgorund image 
#         bg1=Image.open(r"Images_GUI\bg2.jpg")
#         bg1=bg1.resize((1540,768),Image.LANCZOS)
#         self.photobg1=ImageTk.PhotoImage(bg1)

#         # set image as lable
#         bg_img = Label(self.root,image=self.photobg1)
#         bg_img.place(x=0,y=130,width=1540,height=768)


#         #title section
#         title_lb1 = Label(bg_img,text="Welcome to Face Recognition Panel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
#         title_lb1.place(x=0,y=0,width=1540,height=45)

#         # Create buttons below the section 
#         # ------------------------------------------------------------------------------------------------------------------- 
#         # Training button 1
#         std_img_btn=Image.open(r"Images_GUI\f_det.jpg")
#         std_img_btn=std_img_btn.resize((180,180),Image.LANCZOS)
#         self.std_img1=ImageTk.PhotoImage(std_img_btn)

#         std_b1 = Button(bg_img,command=self.face_recog,image=self.std_img1,cursor="hand2")
#         std_b1.place(x=600,y=170,width=180,height=180)

#         std_b1_1 = Button(bg_img,command=self.face_recog,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
#         std_b1_1.place(x=600,y=350,width=180,height=45)
#     #=====================Attendance===================

#     def mark_attendance(self, i, r, n,counter):
#         with open("attendance.csv", "r+", newline="\n") as f:
#             myDatalist = f.readlines()
#             name_list = []
#             for line in myDatalist:
#                 entry = line.split(",")
#                 name_list.append(entry[0])

#             if (i not in name_list) and (r not in name_list) and (n not in name_list):
#                 now = datetime.now()
#                 d1 = now.strftime("%d/%m/%Y")
#                 dtString = now.strftime("%H:%M:%S")
#                 conn = mysql.connector.connect(user='root', password='Jushank@2021',host='localhost',database='face_recognition',port=3306)
#                 cursor = conn.cursor()
#                 cursor.execute("update stdattandance set std_counter = std_counter + 1 where std_id=" + str(id))
#                 counter = list(cursor.fetchone())
#                 counter[0] = int(counter[0])
#                 f.writelines(f"\n{i}, {r}, {n}, {dtString}, {d1}, Present,{counter[0]}")


#     #================face recognition==================
#     def face_recog(self):
#         def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
#             gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#             featuers=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

#             coord=[]
            
#             for (x,y,w,h) in featuers:
#                 cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
#                 id,predict=clf.predict(gray_image[y:y+h,x:x+w])

#                 confidence=int((100*(1-predict/300)))

#                 conn = mysql.connector.connect(user='root', password='Jushank@2021',host='localhost',database='face_recognition',port=3306)
#                 cursor = conn.cursor()

#                 cursor.execute("select Name from student where Student_ID="+str(id))
#                 n=cursor.fetchone()
                

#                 cursor.execute("select Roll_No from student where Student_ID="+str(id))
#                 r=cursor.fetchone()
                

#                 cursor.execute("select Student_ID from student where Student_ID="+str(id))
#                 i=cursor.fetchone()

#                 cursor.execute("select std_counter from stdattandance where std_id=" + str(id))
#                 counter = list(cursor.fetchone())
                


#                 if confidence > 77:
#                     cv2.putText(img,f"Student_ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
#                     cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
#                     cv2.putText(img,f"Roll_No:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
#                     self.mark_attendance(i,r,n,counter)
#                 else:
#                     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
#                     cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)    

#                 coord=[x,y,w,y]
            
#             return coord    


#         #==========
#         def recognize(img,clf,faceCascade):
#             coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
#             return img
        
#         faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#         clf=cv2.face.LBPHFaceRecognizer_create()
#         clf.read("clf.xml")

#         videoCap=cv2.VideoCapture(0)

#         while True:
#             ret,img=videoCap.read()
#             img=recognize(img,clf,faceCascade)
#             cv2.imshow("Face Detector",img)

#             if cv2.waitKey(1) == 13:
#                 break
#         videoCap.release()
#         cv2.destroyAllWindows()




# if __name__ == "__main__":
#     root=Tk()
#     obj=Face_Recognition(root)
#     root.mainloop()


from sys import path
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import mysql.connector
import cv2
from datetime import datetime
import time


class Face_Recognition:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1540x800+0+0")
        self.root.title("Face Recognition Panel")

        # This part is image labels setting start
        # first header image
        img = Image.open(r"D:\College Project\Face-Recognition-Attendence-System\Images_GUI\bku.gif")
        img = img.resize((1540, 200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        # set image as label
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1540, height=200)

        # background image
        bg1 = Image.open(r"Images_GUI\bg2.jpg")
        bg1 = bg1.resize((1540, 800), Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # set image as label
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=200, width=1540, height=800)

        # title section
        title_lb1 = Label(bg_img, text="<--Welcome to Face Recognition Panel-->", font=("verdana", 30, "bold"),
                          bg="white", fg="navyblue")
        title_lb1.place(x=0, y=0, width=1540, height=45)

        # Create buttons below the section
        # -------------------------------------------------------------------------------------------------------------------
        # Training button 1
        std_img_btn = Image.open(r"Images_GUI\f_det.jpg")
        std_img_btn = std_img_btn.resize((400, 400), Image.LANCZOS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img, command=self.face_recog, image=self.std_img1, cursor="hand2")
        std_b1.place(x=600, y=90, width=400, height=400)

        std_b1_1 = Button(bg_img, command=self.face_recog, text="Face Detector", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        std_b1_1.place(x=600, y=450, width=400, height=45)

        # Initialize a set to keep track of marked attendance
        self.attendance_marked = set()
        self.attendance_counts = {}

    

    def mark_attendance(self, i, r, n):
    # Increment the counter for the student ID
        self.attendance_counts[i] = self.attendance_counts.get(i, 0) + 1

        with open("attendance.csv", "a", newline="\n") as f:
            now = datetime.now()
            d1 = now.strftime("%d/%m/%Y")
            dtString = now.strftime("%H:%M")
            
            new_entry = f"\n{i}, {r}, {n}, {dtString}, {d1}, Present, {self.attendance_counts[i]}\n"
            f.write(new_entry)
            

        
   

        

    # def mark_attendance_with_delay(self, i, r, n):
    # # Create a new thread for the attendance marking process
    #     threading.Thread(target=self.mark_attendance, args=(i, r, n)).start()

    # def mark_attendance(self, i, r, n):
    # # Check if attendance is already marked for the student
    #  if i not in self.attendance_marked:
    #     with open("attendance.csv", "r+", newline="\n") as f:
    #         myDatalist = f.readlines()
    #         name_list = []
            
    #         for line in myDatalist:
    #             entry = line.split(",")
    #             name_list.append(entry[0])

    #         if (i not in name_list) and (r not in name_list) and (n not in name_list):
    #             now = datetime.now()
    #             d1 = now.strftime("%d/%m/%Y")
    #             dtString = now.strftime("%H:%M:%S")
    #             self.attendance_counts[i] = self.attendance_counts.get(i, 0) + 1

    #             new_entry = f"\n{i}, {r}, {n}, {dtString}, {d1}, Present, {self.attendance_counts[i]}\n"
    #             f.write(new_entry)

    #         #Add the student ID to the set to mark attendance
    #         self.attendance_counts[i] = self.attendance_counts.get(i, 0) + 1
            

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors,text,color,clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])

                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(user='root', password='Jushank@2021', host='localhost',
                                           database='face_recognition', port=3306)
                cursor = conn.cursor()

                cursor.execute("select Name from student where Student_ID=" + str(id))
                n = cursor.fetchone()

                cursor.execute("select Roll_No from student where Student_ID=" + str(id))
                r = cursor.fetchone()

                cursor.execute("select Student_ID from student where Student_ID=" + str(id))
                i = cursor.fetchone()

                

                # Check if any result is obtained from the database
                if n and r and i:
                    if confidence > 77:
                        cv2.putText(img, f"Student_ID:{i[0]}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                        cv2.putText(img, f"Name:{n[0]}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                        cv2.putText(img, f"Roll-No:{r[0]}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                        self.mark_attendance(i[0], r[0], n[0])
                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)

                    coord = [x, y, w, y]

            return coord

    # ==========
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")

        videoCap = cv2.VideoCapture(0)

        while True:
            ret, img = videoCap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Detector", img)

        # Break the loop if the 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        videoCap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()

