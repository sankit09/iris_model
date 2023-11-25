from flask import Flask, render_template,jsonify,request,url_for
import config
from project_app.utils import Species

app = Flask(__name__)


@app.route("/")
def my_fun():
    print("HEllo Flask")
    return "Lets! Start Predicting The Species"

@app.route('/predict')
def predict():
    data = request.form
    print("Data Is :",data)

    SepalLengthCm = float(data['SepalLengthCm'])
    SepalWidthCm = float(data['SepalWidthCm'])
    PetalLengthCm = float(data['PetalLengthCm'])
    PetalWidthCm = float(data['PetalWidthCm'])

    print('SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm >>>>>',SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)
    
    # Make predictions
    spe_result = Species(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)
    result = spe_result.get_predict_species()

    return jsonify({"Species ":f"Predicted Species is {result}"})
    
    


app.run(debug = True)