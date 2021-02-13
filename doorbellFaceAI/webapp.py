from flask import Flask, redirect, url_for, render_template, request
import numpy as np
import pickle
import os
import re
from faceencode import encodefaces

with open('dataset_faces.dat', 'rb') as f:
	fe = pickle.load(f)

kfn = list(fe.keys())


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/addface", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        print(user)
        return redirect(url_for("user", usr=user))
        print(fe)
    else:
        return render_template("login.html", kfn=kfn)


@app.route("/addnewface/<usr>")
def user(usr):
    submiteduser = {"su": usr}
    formattedlines = """
     print ("Converting and encoding {su}")
     {su}_image = fr.load_image_file("{su}.jpg")
     fe["{su}"] = fr.face_encodings({su}_image)[0]\n\n
    """
    formatted = (formattedlines.format(**submiteduser))

    os.rename('door.jpg',usr + '.jpg')

    with open('faceencode.py', 'r') as fd:
        colinc = 9
        colinc +=3
        data = fd.readlines()
        data[colinc] = formatted

    with open('faceencode.py', 'w') as fd:
        fd.writelines(data)
        fd.close()

    return redirect(url_for("encodestart"))

@app.route("/encodefaces")
def encodestart():
    encodefaces()

    return f"<h1>Encoding!</h1>"

if __name__ == "__main__":
    app.run(debug=False)
