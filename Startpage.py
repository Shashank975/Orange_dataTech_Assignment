from tkinter import *
from PIL import Image, ImageTk
from stdlogin import stdLogin
from login import Login

class Start:
    def __init__(self, root):
        self.root = root
        self.root.title("Start")
        self.root.geometry("1540x800+0+0")

        self.bg_path = r"D:\College Project\Face-Recognition-Attendence-System\Images_GUI\ytr.jpg"
        self.img1_path = r"D:\College Project\Face-Recognition-Attendence-System\Images_GUI\log1.png"

        self.bg = ImageTk.PhotoImage(file=self.bg_path)
        lb1_bg = Label(self.root, image=self.bg)
        lb1_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame1 = Frame(self.root, bg="#002B53")
        frame1.place(x=560, y=170, width=340, height=350)

        self.photoimage1 = ImageTk.PhotoImage(Image.open(self.img1_path).resize((100, 100), Image.LANCZOS))
        self.lb1img1 = Label(image=self.photoimage1, bg="#002B53")
        self.lb1img1.place(x=690, y=175, width=100, height=100)

        get_str = Label(frame1, text="How would you like to Login?", font=("times new roman", 15, "bold"), fg="white", bg="#002B53")
        get_str.place(x=41, y=110)

        # Button for Student Login
        std_login_btn = Button(frame1, text="Student Login", command=self.stdlogin, font=("times new roman", 12), fg="white", bg="#0052cc")
        std_login_btn.place(x=80, y=180, width=180, height=40)

        # Button for Admin Login
        admin_login_btn = Button(frame1, text="Admin Login", command=self.Login, font=("times new roman", 12), fg="white", bg="#0052cc")
        admin_login_btn.place(x=80, y=240, width=180, height=40)

    def stdlogin(self):
        self.new_window = Toplevel(self.root)
        self.app = stdLogin(self.new_window)
        self.new_window.protocol("WM_DELETE_WINDOW", self.on_stdlogin_close)

    def Login(self):
        self.new_window = Toplevel(self.root)
        self.app = Login(self.new_window)
        self.new_window.protocol("WM_DELETE_WINDOW", self.on_login_close)

    def on_stdlogin_close(self):
        self.new_window.destroy()
        self.show_startup_image()

    def on_login_close(self):
        self.new_window.destroy()

    def show_startup_image(self):
        self.lb1img1.destroy()  # Destroy the label containing the image
        self.photoimage1 = ImageTk.PhotoImage(Image.open(self.img1_path).resize((100, 100), Image.LANCZOS))
        self.lb1img1 = Label(image=self.photoimage1, bg="#002B53")
        self.lb1img1.place(x=690, y=175, width=100, height=100)

if __name__ == "__main__":
    root = Tk()
    app = Start(root)
    root.mainloop()
