from tkinter import *
from PIL import ImageTk, Image
import os
import pickle

image_list=[]

def preImage():
    global my_label1
    global button_back1
    global button_forward1
    global present
    global unknown_window
    global total_images
    global button_last_time

    my_label1.grid_forget()
    my_label1 = Label(unknown_window,image=image_list[present - 2])
    present = present - 1
    button_last_time = Button(unknown_window, text="Last Visited Time:  "+last_visited_time[present-1])
    button_last_time.grid(row = 1, column = 0, columnspan = 2)
    if present == total_images - 1:
        button_forward1 = Button(unknown_window, text=">>", command= postImage)
        button_forward1.grid(row=2, column=1)
    if present == 1:
        button_back1 = Button(unknown_window, text="<<", state=DISABLED)
        button_back1.grid(row=2, column=0)
    my_label1.grid(row=0, column = 0, columnspan = 2)
def postImage():
    global my_label1
    global button_back1
    global button_forward1
    global present
    global total_images
    global button_last_time
    global unknown_window

    my_label1.grid_forget()
    my_label1 = Label(unknown_window, image=image_list[present])
    present = present+1
    button_last_time = Button(unknown_window, text="Last Visited Time:  "+last_visited_time[present-1])
    button_last_time.grid(row = 1, column = 0, columnspan=2)
    if present == 2:
        button_back1 = Button(unknown_window, text="<<", command=preImage)
        button_back1.grid(row=2, column=0)
    if present == total_images:
        button_forward1 = Button(unknown_window, text=">>", state = DISABLED)
        button_forward1.grid(row=2, column=1)
    my_label1.grid(row=0, column = 0, columnspan = 2)
def fetchImages(root):
    paths = [os.getcwd()+'\\recognitionfolder\\Unknown\\Unknown_Images\\'+x for x in os.listdir(r'recognitionfolder\Unknown\Unknown_Images')]
    global total_images
    global image_list
    global my_label1
    global button_back1
    global button_forward1
    global present
    global button_last_time
    global unknown_window
    global last_visited_time
    present = 1
    total_images = len(paths)
    if total_images==0:
        return
    else:
        unknown_data = pickle.loads(open('C:/Users/dhana/Desktop/Final Year Work/Face_Recognition_Project/recognitionfolder/Unknown/unknown_face_enc', "rb").read())
        last_visited_time = unknown_data["last_visited_time"]
        unknown_window=Toplevel(root)
        unknown_window.geometry('370x390')
        unknown_window.title('Unknown People Faces')
        image_list = []
        for i in paths:
            image_list.append(ImageTk.PhotoImage(Image.open(i).resize((300, 300), Image.ANTIALIAS)))
        my_label1 = Label(unknown_window, image=image_list[0])
        my_label1.grid(row=0, column=0, columnspan=2)
        button_back1 = Button(unknown_window, text="<<", state=DISABLED)
        button_back1.grid(row=2, column=0)
        if total_images == 1:
            button_forward1 = Button(unknown_window, text=">>", state=DISABLED)
        else:
            button_forward1 = Button(unknown_window, text=">>", command=postImage)
        button_forward1.grid(row=2, column=1)
        button_last_time = Button(unknown_window, text="Last Visited Time:  "+last_visited_time[present-1])
        button_last_time.grid(row = 1, column = 0, columnspan=2)
