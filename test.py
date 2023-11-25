from flask import Flask,jsonify,request,render_template,redirect,url_for
from project_app.utils import Species
app = Flask(__name__)


@app.route("/")   #home API

def my_fun():
    print("Hello Flask")
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():

    SepalLengthCm = float(request.form['SepalLengthCm'])
    SepalWidthCm = float(request.form['SepalWidthCm'])
    PetalLengthCm = float(request.form['PetalLengthCm'])
    PetalWidthCm = float(request.form['PetalWidthCm'])

    prediction = Species(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)
    result = prediction.get_predict_species()
    return render_template('index.html', prediction=result)

app.run(debug = False,host='0.0.0.0')