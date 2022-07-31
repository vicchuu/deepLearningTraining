import tensorflow.python.keras
from flask import Flask , render_template

from flask_wtf import FlaskForm

from wtforms import FileField ,SubmitField
import cv2
from PIL import Image
import numpy as np
from werkzeug.utils import secure_filename
import os
import tensorflow as tf
from keras.models import load_model
from flask_wtf.csrf import CSRFProtect, CSRFError
app = Flask(__name__)
csrf = CSRFProtect(app)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config["UPLOAD_FOLDER"] = 'temp/files'

classes = { 0:'Speed limit (20km/h)',
            1:'Speed limit (30km/h)',
            2:'Speed limit (50km/h)',
            3:'Speed limit (60km/h)',
            4:'Speed limit (70km/h)',
            5:'Speed limit (80km/h)',
            6:'End of speed limit (80km/h)',
            7:'Speed limit (100km/h)',
            8:'Speed limit (120km/h)',
            9:'No passing',
            10:'No passing veh over 3.5 tons',
            11:'Right-of-way at intersection',
            12:'Priority road',
            13:'Yield',
            14:'Stop',
            15:'No vehicles',
            16:'Veh > 3.5 tons prohibited',
            17:'No entry',
            18:'General caution',
            19:'Dangerous curve left',
            20:'Dangerous curve right',
            21:'Double curve',
            22:'Bumpy road',
            23:'Slippery road',
            24:'Road narrows on the right',
            25:'Road work',
            26:'Traffic signals',
            27:'Pedestrians',
            28:'Children crossing',
            29:'Bicycles crossing',
            30:'Beware of ice/snow',
            31:'Wild animals crossing',
            32:'End speed + passing limits',
            33:'Turn right ahead',
            34:'Turn left ahead',
            35:'Ahead only',
            36:'Go straight or right',
            37:'Go straight or left',
            38:'Keep right',
            39:'Keep left',
            40:'Roundabout mandatory',
            41:'End of no passing',
            42:'End no passing veh > 3.5 tons' }


#app.config["SECRECT_KEY"]= 'superkey'

class uploadFile(FlaskForm):
    file =  FileField("File")


    submit = SubmitField("Upload File")



@app.route("/",methods=['GET','POST'])
@app.route("/home",methods=['GET','POST'])
def homePage():
    form = uploadFile()

    if form.validate_on_submit():
        file = form.file.data

        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config["UPLOAD_FOLDER"],secure_filename(file.filename)))
        image = cv2.imread(app.config["UPLOAD_FOLDER"] + "/" + file.filename)
        print("path :", (app.config["UPLOAD_FOLDER"] + "/" + file.filename))
        ans = imageArray(image)
        return ("predicted image is :  "+ans)
    return render_template("index.html",form = form)


def imageArray(image):
    data = []
    try:
        #image =
        image_fromArray = Image.fromarray(image, "RGB")
        resize_img = image_fromArray.resize((30, 30))
        data.append(np.array(resize_img))
    except:
        print("issue in img ", image)

    x_test1 = np.array(data)
    model_img = load_model("traffic_signal_classify.h5")
    predicted_label = model_img.predict(x_test1)
    classes_predict = tf.argmax(predicted_label, axis=1)
    index = (int( classes_predict[0] ))
    print(index ,type(index))
    #print(classes_predict[0])
    print("Prediction :", classes[index])
    return classes[index]

if __name__=="__main__":
    app.run(debug=True)



