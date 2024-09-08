import pickle
data = {"encodings":[], "file_names":[], "last_visited_time":[]}

f = open("unknown_face_enc", "wb")
f.write(pickle.dumps(data))
f.close()
