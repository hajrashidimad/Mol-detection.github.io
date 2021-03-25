from flask import Flask, render_template, request, url_for
import os
from model import *
from tensorflow.keras.models import load_model, model_from_json
import tensorflow as tf

tf.debugging.set_log_device_placement(True)



# init flask app 
my_app = Flask(__name__)
folder = "/home/imad/Desktop/Becode/Project/challenge-mole/deployment/static"




@my_app.route("/", methods=["POST", "GET"])
def uplaod():
    if request.method == "POST" : 
        image = request.files["image"]
        if image:
            image_location = os.path.join(folder,image.filename)
            image.save(image_location)
            pred = model.predict(prepare(image_location))
            response = category[int(pred[0][0])]
            if response == "cancerous":
                response = " WARNING !!: UNFORTUNATELY! we advice you to contact your AS SOON AS possible, according our indicators the level of risk is high."
            
            elif response == "not_cancerous":
                response = "CONGRATULATIONS !! there is no risk for your skin, the level of risk is low"

        else:
            response = "No prediction detected yet"
    elif request.method == "GET":
        response = "No prediction detected yet"



    return render_template("index.html", prediction=response)

    

@my_app.route("/test", methods=["POST", "GET"])
def test():
    if request.method == "POST" : 
        image = request.files["image"]
        if image:
            image_location = os.path.join(folder,image.filename)
            image.save(image_location)
            # pred = predict(image_location, MODEL)
            pred = model.predict(prepare(image_location))
            response = category[int(pred[0][0])]
            if response == "cancerous":
                response = " WARNING !!: UNFORTUNATELY! we advice you to contact your AS SOON AS possible, according our indicators the level of risk is high."
            
            elif response == "not_cancerous":
                response = "CONGRATULATIONS !! there is no risk for your skin, the level of risk is low"

        else:
            response = "No prediction detected yet"
    elif request.method == "GET":
        response = "No prediction detected yet"



    return render_template("pred.html", prediction=response)

if __name__ == "__main__":
    my_app.run(host="127.0.0.1", port=8000, debug=True)

#python my_app.py