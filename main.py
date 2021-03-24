from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

def delete_uploaded_image(path):
    os.remove(path)
    # return "Deleted"

def predict_image(path):
    # After Processing, Delete the File
    # delete_uploaded_image(path) 
    return path


@app.route("/", methods = ["POST", "GET"])
def index():
    
    if request.method == "POST":
        file = request.files["image"]
        file.save(os.path.join("uploads", file.filename))
        path = "./uploads/" + file.filename
        return render_template("index.html", message = predict_image(path))        
    return render_template("index.html", message = "Please Upload File!")

if __name__ == "__main__":
    app.run(debug = True)