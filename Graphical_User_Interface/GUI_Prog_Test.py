import tkinter as GUI
from tkinter import *
from PIL import Image, ImageTk
from beta import *
from omega import *


def show_frame(frame):
    frame.tkraise()


def GUI_func():
    root = GUI.Tk()
    root.geometry("1920x1080")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.title('Library GUI')

    frameMain = GUI.Frame(root)
    frameDirect = GUI.Frame(root)
    frameResEnq = GUI.Frame(root)
    frameResLoc = GUI.Frame(root)
    frameLibEnq = GUI.Frame(root)
    frameResEnqAns1 = GUI.Frame(root)
    frameResEnqAns2 = GUI.Frame(root)
    frameResEnqAns3 = GUI.Frame(root)
    frameResEnqAns4 = GUI.Frame(root)
    frameResEnqAns5 = GUI.Frame(root)
    frameLibEnqAns1 = GUI.Frame(root)
    frameLibEnqAns2 = GUI.Frame(root)
    frameLibEnqAns3 = GUI.Frame(root)
    frameLibEnqAns4 = GUI.Frame(root)
    frameLibEnqAns5 = GUI.Frame(root)

# Logo
    logo = Image.open('logo.png')
    logo = ImageTk.PhotoImage(logo)
    logo_label = GUI.Label(frameMain, image=logo)
    logo_label.image = logo
    logo_label.place(x=775, y=100)

    for frame in (frameMain, frameDirect, frameResEnq, frameResLoc, frameLibEnq, frameResEnqAns1,
                  frameResEnqAns2, frameResEnqAns3, frameResEnqAns4, frameResEnqAns5, frameLibEnqAns1,
                  frameLibEnqAns2, frameLibEnqAns3, frameLibEnqAns4, frameLibEnqAns5):
        frame.grid(row=0, column=0, sticky='nsew')

    def Button_Func_frame(frame1, write, fontType, fontSize, color, h, w, frame2, xloc, yloc):
        frame_btn = GUI.Button(frame1, text=write, font=(
            'Arial', fontSize), bg='indian red', height=h, width=w, command=lambda: show_frame(frame2))
        frame_btn.place(x=xloc, y=yloc)

    def Button_Func_move(frame1, write, fontType, fontSize, color, h, w, xloc, yloc):
        frame_btn = GUI.Button(frame1, text=write, font=(
            fontType, fontSize), bg=color, height=h, width=w, command=lambda: print("Moving to Location"))
        frame_btn.place(x=xloc, y=yloc)

    def Label_func(frame1, write, fontType, fontSize, xloc, yloc):
        frame_title = GUI.Label(frame1, text=write, font=(fontType, fontSize))
        frame_title.place(x=xloc, y=yloc)

# Instructions
    Label_func(frameMain, 'Please select your Enquiry', 'Arial', 36, 680, 260)
    # ========Directory=============

    Button_Func_frame(frameMain, 'Directory', 'Arial', 18,
                      'indian red', 4, 30, frameDirect, 560, 360)

    Label_func(frameDirect, 'Welcome to the Directory', 'Arial', 36, 680, 50)

    Button_Func_frame(frameDirect, 'Back to Main Page', 'Arial',
                      14, 'indian red', 2, 20, frameMain, 800, 950)

    Button_Func_move(frameDirect, 'Project Hub', 'Arial',
                     14, 'indian red', 2, 20, 800, 250)

    Button_Func_move(frameDirect, 'Store', 'Arial',
                     14, 'indian red', 2, 20, 800, 200)

    Button_Func_move(frameDirect, 'Discussion Rooms', 'Arial',
                     14, 'indian red', 2, 20, 800, 150)

    Button_Func_move(frameDirect, 'Relaxation Rooms', 'Arial',
                     14, 'indian red', 2, 20, 800, 100)

    # ================================

    # ========Resource Enquiry========

    Button_Func_frame(frameMain, 'Resource Enquiry', 'Arial',
                      18, 'indian red', 4, 30, frameResEnq, 560, 490)

    Label_func(frameResEnq, 'Welcome to Resource Enquiry',
               'Arial', 36, 640, 50)

    Button_Func_frame(frameResEnq, 'Back to Main Page', 'Arial',
                      14, 'indian red', 2, 20, frameMain, 800, 950)

    Button_Func_frame(frameResEnq, 'Question 1', 'Arial', 14,
                      'indian red', 2, 80, frameResEnqAns1, 550, 100)

    Label_func(frameResEnqAns1, 'Answer 1', 'Arial', 36, 840, 50)

    Button_Func_frame(frameResEnqAns1, 'Back to Main Page', 'Arial',
                      14, 'indian red', 2, 20, frameMain, 800, 950)

    Button_Func_frame(frameResEnq, 'Question 2', 'Arial', 14,
                      'indian red', 2, 80, frameResEnqAns2, 550, 160)

    Label_func(frameResEnqAns2, 'Answer 2', 'Arial', 36, 840, 50)

    Button_Func_frame(frameResEnqAns2, 'Back to Main Page', 'Arial',
                      14, 'indian red', 2, 20, frameMain, 800, 950)

    Button_Func_frame(frameResEnq, 'Question 3', 'Arial', 14,
                      'indian red', 2, 80, frameResEnqAns3, 550, 220)

    Label_func(frameResEnqAns3, 'Answer 3', 'Arial', 36, 840, 50)

    Button_Func_frame(frameResEnqAns3, 'Back to Main Page', 'Arial',
                      14, 'indian red', 2, 20, frameMain, 800, 950)

    Button_Func_frame(frameResEnq, 'Question 4', 'Arial', 14,
                      'indian red', 2, 80, frameResEnqAns4, 550, 280)

    Label_func(frameResEnqAns4, 'Answer 4', 'Arial', 36, 840, 50)

    Button_Func_frame(frameResEnqAns4, 'Back to Main Page', 'Arial',
                      14, 'indian red', 2, 20, frameMain, 800, 950)

    Button_Func_frame(frameResEnq, 'Question 5', 'Arial', 14,
                      'indian red', 2, 80, frameResEnqAns5, 550, 340)

    Label_func(frameResEnqAns5, 'Answer 5', 'Arial', 36, 840, 50)

    Button_Func_frame(frameResEnqAns5, 'Back to Main Page', 'Arial',
                      14, 'indian red', 2, 20, frameMain, 800, 950)
    # ================================

    # ========Library Enquiry========

    Button_Func_frame(frameMain, 'Library Enquiry', 'Arial',
                      18, 'indian red', 4, 30, frameLibEnq, 980, 360)

    Label_func(frameLibEnq, 'Welcome to Library Enquiry', 'Arial', 36, 640, 50)

    Button_Func_frame(frameLibEnq, 'Back to Main Page', 'Arial',
                      14, 'indian red', 2, 20, frameMain, 800, 950)

    Button_Func_frame(frameLibEnq, 'Question 1', 'Arial', 14,
                      'indian red', 2, 80, frameLibEnqAns1, 550, 100)

    Label_func(frameLibEnqAns1, 'Answer 1', 'Arial', 36, 840, 50)

    Button_Func_frame(frameLibEnqAns1, 'Back to Main Page', 'Arial',
                      14, 'indian red', 2, 20, frameMain, 800, 950)

    Button_Func_frame(frameLibEnq, 'Question 2', 'Arial', 14,
                      'indian red', 2, 80, frameLibEnqAns2, 550, 160)

    Label_func(frameLibEnqAns2, 'Answer 2', 'Arial', 36, 840, 50)

    Button_Func_frame(frameLibEnqAns2, 'Back to Main Page', 'Arial',
                      14, 'indian red', 2, 20, frameMain, 800, 950)

    Button_Func_frame(frameLibEnq, 'Question 3', 'Arial', 14,
                      'indian red', 2, 80, frameLibEnqAns3, 550, 220)

    Label_func(frameLibEnqAns3, 'Answer 3', 'Arial', 36, 840, 50)

    Button_Func_frame(frameLibEnqAns3, 'Back to Main Page', 'Arial',
                      14, 'indian red', 2, 20, frameMain, 800, 950)

    Button_Func_frame(frameLibEnq, 'Question 4', 'Arial', 14,
                      'indian red', 2, 80, frameLibEnqAns4, 550, 280)

    Label_func(frameLibEnqAns4, 'Answer 4', 'Arial', 36, 840, 50)

    Button_Func_frame(frameLibEnqAns4, 'Back to Main Page', 'Arial',
                      14, 'indian red', 2, 20, frameMain, 800, 950)

    Button_Func_frame(frameLibEnq, 'Question 5', 'Arial', 14,
                      'indian red', 2, 80, frameLibEnqAns5, 550, 340)

    Label_func(frameLibEnqAns5, 'Answer 1', 'Arial', 36, 840, 50)

    Button_Func_frame(frameLibEnqAns5, 'Back to Main Page', 'Arial',
                      14, 'indian red', 2, 20, frameMain, 800, 950)
    # ================================

    # ========Resource Locator=======

    Button_Func_frame(frameMain, 'Resource Locator', 'Arial',
                      18, 'indian red', 4, 30, frameResLoc, 980, 490)

    Label_func(frameResLoc, 'Welcome to Resource Locator',
               'Arial', 36, 640, 50)

    Button_Func_frame(frameResLoc, 'Back to Main Page', 'Arial',
                      14, 'indian red', 2, 20, frameMain, 800, 950)
# ================================

    show_frame(frameMain)
    root.mainloop()
