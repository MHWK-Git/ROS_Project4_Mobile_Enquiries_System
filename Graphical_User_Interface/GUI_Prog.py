#!/usr/bin/env python3

import tkinter as GUI
from tkinter import *
from PIL import Image, ImageTk
from waypoint import *


def show_frame(frame):
    frame.tkraise()


def GUI_func():
    root = GUI.Tk()
    root.attributes('-fullscreen', True)
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

    def MoveTo(x_pos, y_pos, z_ori, w_ori):
        rospy.sleep(0.1)
        Waypoint_Client(x_pos, y_pos, z_ori, w_ori)
        rospy.sleep(0.1)
        frameMain.tkraise()
        rospy.sleep(5.0)
        Waypoint_Client(0.0, 0.0, 0.0, 0.1)
        rospy.sleep(0.1)

# Logo
    logo = Image.open('agilex_ws/src/limo_ros/limo_bringup/scripts/logo.png')
    logo = ImageTk.PhotoImage(logo)
    logo_label = GUI.Label(frameMain, image=logo)
    logo_label.image = logo
    logo_label.place(x=300, y=40)

    for frame in (frameMain, frameDirect, frameResEnq, frameResLoc, frameLibEnq, frameResEnqAns1, frameResEnqAns2, frameResEnqAns3,
                  frameResEnqAns4, frameResEnqAns5, frameLibEnqAns1, frameLibEnqAns2,  frameLibEnqAns3, frameLibEnqAns4, frameLibEnqAns5):
        frame.grid(row=0, column=0, sticky='nsew')

    def Button_Func_frame(frame1, write, fontType, fontSize, color, h, w, frame2, xloc, yloc):
        frame_btn = GUI.Button(frame1, text=write, font=(
            fontType, fontSize), bg='indian red', height=h, width=w, command=lambda: show_frame(frame2))
        frame_btn.place(x=xloc, y=yloc)

    def Button_Func_move(frame1, write, fontType, fontSize, color, h, w, xpos, ypos, zori, wori, xloc, yloc):
        frame_btn = GUI.Button(frame1, text=write, font=(
            fontType, fontSize), bg=color, height=h, width=w, command=lambda: MoveTo(xpos, ypos, zori, wori))
        frame_btn.place(x=xloc, y=yloc)

    def Label_func(frame1, write, fontType, fontSize, xloc, yloc):
        frame_title = GUI.Label(frame1, text=write, font=(fontType, fontSize))
        frame_title.place(x=xloc, y=yloc)

# Instructions
    Label_func(frameMain, "Please select your Enquiry", 'Arial', 34, 220, 190)

    # ========Directory==============
    Button_Func_frame(frameMain, 'Directory', 'Arial', 18,
                      'indian red', 4, 20, frameDirect, 200, 250)
    Label_func(frameDirect, "Welcome to the Directory", 'Arial', 20, 350, 30)

    Quit_btn = GUI.Button(frameMain, text='Quit', font=(
        'Arial', 14), bg='indian red', height=2, width=20, command=lambda: root.destroy())
    Quit_btn.place(x=380, y=520)

    Button_Func_move(frameDirect, 'Project Hub', 'Arial', 18,
                     'indian red', 4, 20, 1.0, 0.5, 0.0, 1.0, 200, 150)
    Button_Func_move(frameDirect, 'Store', 'Arial', 18,
                     'indian red', 4, 20, 0.5, 1.0, 0.0, 1.0, 500, 150)
    Button_Func_move(frameDirect, 'Discussion Rooms', 'Arial',
                     18, 'indian red', 4, 20, -1.35, 1.0, 0.0, 1.0, 200, 280)
    Button_Func_move(frameDirect, 'Relaxation Area', 'Arial',
                     18, 'indian red', 4, 20, 1.0, 1.0, 0.0, 1.0, 500, 280)
    Button_Func_frame(frameDirect, 'Back to Main Page', 'Arial',
                      14, 'indian red', 2, 20, frameMain, 380, 500)
    # ================================

    # ========Resource Enquiry=========
    Button_Func_frame(frameMain, 'Resource Enquiry', 'Arial',
                      18, 'indian red', 4, 20, frameResEnq, 200, 380)
    Label_func(frameResEnq, "Welcome to Resource Enquiry",
               'Arial', 20, 320, 30)

    Button_Func_frame(frameResEnq, 'Back to Main Page', 'Arial',
                      14, 'indian red', 2, 20, frameMain, 380, 520)
    Button_Func_frame(frameResEnqAns1, 'Back to Main Page',
                      'Arial', 14, 'indian red', 2, 20, frameMain, 380, 520)
    Button_Func_frame(frameResEnqAns2, 'Back to Main Page',
                      'Arial', 14, 'indian red', 2, 20, frameMain, 380, 520)
    Button_Func_frame(frameResEnqAns3, 'Back to Main Page',
                      'Arial', 14, 'indian red', 2, 20, frameMain, 380, 520)
    Button_Func_frame(frameResEnqAns4, 'Back to Main Page',
                      'Arial', 14, 'indian red', 2, 20, frameMain, 380, 520)
    Button_Func_frame(frameResEnqAns5, 'Back to Main Page',
                      'Arial', 14, 'indian red', 2, 20, frameMain, 380, 520)

    Button_Func_frame(frameResEnq, 'How are the resources sorted online?',
                      'Arial', 12, 'indian red', 2, 60, frameResEnqAns1, 220, 80)
    Button_Func_frame(frameResEnq, 'How are the books sorted in the library?',
                      'Arial', 12, 'indian red', 2, 60, frameResEnqAns2, 220, 160)
    Button_Func_frame(frameResEnq, 'What can I do if I cannot find certain material?',
                      'Arial', 12, 'indian red', 2, 60, frameResEnqAns3, 220, 240)
    Button_Func_frame(frameResEnq, 'How long can I borrow the materials for?',
                      'Arial', 12, 'indian red', 2, 60, frameResEnqAns4, 220, 320)
    Button_Func_frame(frameResEnq, 'How do I borrow materials?',
                      'Arial', 12, 'indian red', 2, 60, frameResEnqAns5, 220, 400)

    Label_func(frameResEnqAns1, 'Answer 1', 'Arial', 20, 340, 30)
    Label_func(frameResEnqAns2, 'Answer 2', 'Arial', 20, 340, 30)
    Label_func(frameResEnqAns3, 'Answer 3', 'Arial', 20, 340, 30)
    Label_func(frameResEnqAns4, 'Answer 4', 'Arial', 20, 340, 30)
    Label_func(frameResEnqAns5, 'Answer 5', 'Arial', 20, 340, 30)
    # ================================

    # ========Library Enquiry===========
    Button_Func_frame(frameMain, 'Library Enquiry', 'Arial',
                      18, 'indian red', 4, 20, frameLibEnq, 500, 250)
    Label_func(frameLibEnq, "Welcome to Library Enquiry", 'Arial', 20, 320, 30)

    Button_Func_frame(frameLibEnq, 'Back to Main Page', 'Arial',
                      14, 'indian red', 2, 20, frameMain, 380, 520)
    Button_Func_frame(frameLibEnqAns1, 'Back to Main Page',
                      'Arial', 14, 'indian red', 2, 20, frameMain, 380, 520)
    Button_Func_frame(frameLibEnqAns2, 'Back to Main Page',
                      'Arial', 14, 'indian red', 2, 20, frameMain, 380, 520)
    Button_Func_frame(frameLibEnqAns3, 'Back to Main Page',
                      'Arial', 14, 'indian red', 2, 20, frameMain, 380, 520)
    Button_Func_frame(frameLibEnqAns4, 'Back to Main Page',
                      'Arial', 14, 'indian red', 2, 20, frameMain, 380, 520)
    Button_Func_frame(frameLibEnqAns5, 'Back to Main Page',
                      'Arial', 14, 'indian red', 2, 20, frameMain, 380, 520)

    Button_Func_frame(frameLibEnq, 'What are the opening hours of the library?',
                      'Arial', 12, 'indian red', 2, 60, frameLibEnqAns1, 220, 80)
    Button_Func_frame(frameLibEnq, 'Are there any fines for late returning?',
                      'Arial', 12, 'indian red', 2, 60, frameLibEnqAns2, 220, 160)
    Button_Func_frame(frameLibEnq, 'Is there any communication channel I can contact for requests?',
                      'Arial', 12, 'indian red', 2, 60, frameLibEnqAns3, 220, 240)
    Button_Func_frame(frameLibEnq, 'How do I book the rooms and facilities?',
                      'Arial', 12, 'indian red', 2, 60, frameLibEnqAns4, 220, 320)
    Button_Func_frame(frameLibEnq, 'Are there any storage units in the library?',
                      'Arial', 12, 'indian red', 2, 60, frameLibEnqAns5, 220, 400)

    Label_func(frameLibEnqAns1, 'Answer 1', 'Arial', 20, 340, 30)
    Label_func(frameLibEnqAns2, 'Answer 2', 'Arial', 20, 340, 30)
    Label_func(frameLibEnqAns3, 'Answer 3', 'Arial', 20, 340, 30)
    Label_func(frameLibEnqAns4, 'Answer 4', 'Arial', 20, 340, 30)
    Label_func(frameLibEnqAns5, 'Answer 5', 'Arial', 20, 340, 30)
    # ================================

    # ========Resource Locator==========
    Button_Func_frame(frameMain, 'Resource Locator', 'Arial',
                      18, 'indian red', 4, 20, frameResLoc, 500, 380)
    Label_func(frameResLoc, "Welcome to Resource Locator",
               'Arial', 20, 320, 30)

    Button_Func_move(frameResLoc, 'Business\nManagement', 'Arial',
                     16, 'indian red', 2, 20, 2.0, 0.5, 0.0, 1.0, 250, 90)
    Button_Func_move(frameResLoc, 'Medicine', 'Arial', 16,
                     'indian red', 2, 20, 2.0, 0.5, 0.0, 1.0, 530, 90)
    Button_Func_move(frameResLoc, 'Econs and Finance', 'Arial',
                     16, 'indian red', 2, 20, 2.0, 0.5, 0.0, 1.0, 250, 160)
    Button_Func_move(frameResLoc, 'Education', 'Arial', 16,
                     'indian red', 2, 20, 2.0, 0.5, 0.0, 1.0, 530, 160)
    Button_Func_move(frameResLoc, 'Chemistry', 'Arial', 16,
                     'indian red', 2, 20, 2.0, 0.5, 0.0, 1.0, 250, 230)
    Button_Func_move(frameResLoc, 'Material\nScience', 'Arial',
                     16, 'indian red', 2, 20, 2.0, 0.5, 0.0, 1.0, 530, 230)
    Button_Func_move(frameResLoc, 'Engineering', 'Arial', 16,
                     'indian red', 2, 20, 2.0, 0.5, 0.0, 1.0, 250, 300)
    Button_Func_move(frameResLoc, 'Comp Science', 'Arial', 16,
                     'indian red', 2, 20, 2.0, 0.5, 0.0, 1.0, 530, 300)

    Button_Func_frame(frameResLoc, 'Back to Main Page', 'Arial',
                      14, 'indian red', 2, 20, frameMain, 380, 520)
# ================================

    show_frame(frameMain)
    root.mainloop()
