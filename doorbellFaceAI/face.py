import face_recognition as fr
import cv2
import pickle
import numpy as np
from msg import msg, unknown
import webapp


#Known face encodings
#kfe = [
 # levi_fe,
  #obama_fe,
  #biden_fe
#]

# Load face encodings
with open('dataset_faces.dat', 'rb') as f:
	fe = pickle.load(f)

# Grab the list of names and the list of encodings
kfn = list(fe.keys())
kfe = np.array(list(fe.values()))

#Knwon face encodings names
#kfn = [
# "levi",
# "obama",
# "biden"
#]

#video feed to recognize
videofeed = cv2.VideoCapture(0)
print("video feed on")

print ("Converting and encoding")
while True:
    ret, frame = videofeed.read()
    rgb_frame = frame[:, :, ::-1]
    flf = fr.face_locations(rgb_frame)
    fef = fr.face_encodings(rgb_frame, flf)

    for (top, right, bottom, left), face_encoding in zip(flf, fef):
        matches = fr.compare_faces(kfe, face_encoding)
        name = "Unkown"
        print("looking..")

        if True in matches:
            first_match_index = matches.index(True)
            name = kfn[first_match_index]
            print(name)
            if name == 'levi':
              msg(name)
              exit()
            elif name == 'obama':
              msg(name)
              exit()

        else:
            print(name)
            ret,frame = videofeed.read()
            cv2.imshow('img1',frame) #display the captured image
            cv2.imwrite('door.jpg',frame)
            unknown('Unkown face at door')
            exit()
