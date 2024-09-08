import face_recognition
import imutils
import pickle
import time
import notify
import cv2
import os
from datetime import datetime


# load the known faces and embeddings saved in last file
data = pickle.loads(open('C:/Users/dhana/Desktop/Final Year Work/Face_Recognition_Project/recognitionfolder/face_enc', "rb").read())
def recognizeFaces(frame, rgb_frame, face_boxes):
    names = []
    boxes_return = []
    result = []
    encodings = face_recognition.face_encodings(rgb_frame, face_boxes)
    # the facial embeddings for face in input
    # loop over the facial embeddings incase
    # we have multiple embeddings for multiple faces
    if len(encodings) < len(face_boxes):
        result.append(boxes_return)
        result.append(names)
        return result
    for idx, encoding in enumerate(encodings):
        unknown_data = pickle.loads(open('C:/Users/dhana/Desktop/Final Year Work/Face_Recognition_Project/recognitionfolder/Unknown/unknown_face_enc', "rb").read())
       #Compare encodings with encodings in data["encodings"]
       #Matches contain array with boolean values and True for the embeddings it matches closely
       #and False for rest
        matches = face_recognition.compare_faces(data["encodings"],
         encoding)
        #set name =Unknown if no encoding matches
        name = ""
        # check to see if we have found a match
        if True in matches:
            #Find positions at which we get True and store them
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}
            # loop over the matched indexes and maintain a count for
            # each recognized face face
            for i in matchedIdxs:
                #Check the names at respective indexes we stored in matchedIdxs
                name = data["names"][i]
                #increase count for the name we got
                counts[name] = counts.get(name, 0) + 1
            #set name which has highest count
            name = max(counts, key=counts.get)
        else:
            match_unknown = face_recognition.compare_faces(unknown_data["encodings"],encoding)
            if True in match_unknown:
                matchedIdxs = [i for (i, b) in enumerate(match_unknown) if b]
                #set name which has highest count
                index = matchedIdxs[0]
                unknown_data["last_visited_time"][index] = datetime.now().strftime('%d %b %Y  %X')
                name = "Unknown"
            else:
                lenn = len(match_unknown)
                notify.sendMessage()
                unknown_data["encodings"].append(encoding)
                unknown_data["file_names"].append(str(lenn)+".jpg")
                unknown_data["last_visited_time"].append(datetime.now().strftime('%d %b %Y  %X'))
                name = "Unknown"
                face_box_temp = face_boxes[idx]
                t1 = face_box_temp[0]
                t2 = face_box_temp[1]
                t3 = face_box_temp[2]
                t4 = face_box_temp[3]
                save_frame = frame[t1:t3, t4:t2]
                path = r'C:\Users\dhana\Desktop\Final Year Work\Face_Recognition_Project\recognitionfolder\Unknown\Unknown_Images'
                cv2.imwrite(path+"\\"+str(lenn)+".jpg", save_frame)
        names.append(name)
        boxes_return.append(face_boxes[idx])
        f = open("C:/Users/dhana/Desktop/Final Year Work/Face_Recognition_Project/recognitionfolder/Unknown/unknown_face_enc", "wb")
        f.write(pickle.dumps(unknown_data))
        f.close()
    result.append(names)
    result.append(boxes_return)
    print(unknown_data['last_visited_time'])
    return result
