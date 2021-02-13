import face_recognition as fr
import pickle

fe = {}

#known faces
def encodefaces():






     print ("Converting and encoding levi")
     levi_image = fr.load_image_file("levi.jpg")
     fe["levi"] = fr.face_encodings(levi_image)[0]


    



     print ("Converting and encoding 2")
     obama_image = fr.load_image_file("obama.jpg")
     fe["obama"] = fr.face_encodings(obama_image)[0]

     print ("Converting and encoding 3")
     biden_image = fr.load_image_file("biden.jpg")
     fe["biden"] = fr.face_encodings(biden_image)[0]

     # ... etc ...

     with open('dataset_faces.dat', 'wb') as f:
         pickle.dump(fe, f)



encodefaces()
