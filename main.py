from imutils.video import VideoStream
from tkinter import *
from PIL import ImageTk, Image
import time
import cv2
from recognitionfolder.recognize import recognizeFaces
import notify
import face_recognition
import displayUnknown

print("[INFO] Printing to console")
print()
notify.sendStart()
print("[INFO] System Ready")
print()
print("[INFO] Press 'q' to exit")
print()
root=Tk()
root.title('Security System')
root.geometry('650x520')
window1 = Frame(root)
intro_img = ImageTk.PhotoImage(Image.open("intro.jpg"))
my_label = Label(window1, image = intro_img)
my_label.grid(row = 0, column = 0, columnspan = 2)
button_view_unknown = Button(window1, text="View Unknown People", command=lambda: displayUnknown.fetchImages(root))
button_view_unknown.grid(row = 1, column=1)
button_exit = Button(window1, text="Exit", state=DISABLED)
button_exit.grid(row = 1, column=0)
window1.grid(row=0, column=0)
window1.tkraise()
# initialize the video stream and allow the camera sensor to warm up(3 secs)
print("[INFO] Starting video stream")
vs = VideoStream(src=0).start()
time.sleep(1.0)
# loop over the frames from the video stream
def mainFunc():
    global my_label
    global window1
    global display_image
    frame = vs.read()
    rgb_frame = frame[:, :, ::-1]
    face_boxes = face_recognition.face_locations(rgb_frame,number_of_times_to_upsample=0)
    if len(face_boxes) > 0:
        result = recognizeFaces(frame, rgb_frame, face_boxes)
        if len(result[0])>0:
            res_len = len(result[0])
            names_display = result[0]
            boxes_display = result[1]
            for i in range(0, res_len):
                x = boxes_display[i][3]
                y = boxes_display[i][0]
                right = boxes_display[i][1]
                bottom = boxes_display[i][2]
                cv2.rectangle(frame, (x, y), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, names_display[i], (x, y), cv2.FONT_HERSHEY_SIMPLEX,0.75, (0, 255, 0), 2)
    display_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    display_image = Image.fromarray(display_image)
    display_image = ImageTk.PhotoImage(display_image)
    my_label.grid_forget()
    my_label = Label(window1, image = display_image)
    my_label.grid(row = 0, column = 0, columnspan=2)
    root.after(100, mainFunc)
def showStartup():
    mainFunc()
root.after(3000, showStartup)
#root.mainloop()
#cv2.destroyAllWindows()
