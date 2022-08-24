from flask import Flask, flash, render_template, request, redirect
from predict import predict_image

UPLOAD_FOLDER = "./file/image-upload"



app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def input_image():
    if request.method == "POST":
        file = request.files.get("file")
        # for API
        response = predict_image(file)
        return f"{response}"
    return render_template("index.html")



if __name__ == '__main__': app.run(debug=True)