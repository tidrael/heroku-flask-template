from flask import Flask, flash, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from flask_bootstrap import Bootstrap
from predict import predict_image

UPLOAD_FOLDER = "./file/image-upload"

class ImageForm(FlaskForm):
    image = FileField(label='Image input')
    submit = SubmitField(label="Submit")


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/input-image", methods=["GET", "POST"])
def input_image():
    if request.method == "POST":
        file = request.files.get("file")
        # for API
        response = predict_image(file)
        return f"{response}"
    return render_template("img-input.html")



if __name__ == '__main__': app.run(debug=True)