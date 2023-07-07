from flask import Flask,request,render_template,url_for
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib as joblib
import os

model=joblib.load('CovidLabDetect-kh-ABST.pkl')

app =Flask(__name__)

IMG_FOLDER=os.path.join('static','IMG')
app.config['UPLOAD_FOLDER']=IMG_FOLDER


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['GET','POST'])
def home():
    if request.method =='POST':
        age = float(request.form['Age'])
        gndr = float(request.form['Gender'])
        antib = float(request.form['Antibiotics'])
        para = float(request.form['Paracetamol'])
        ox = float(request.form['oxygen'])
        vent = float(request.form['Ventilated'])
        rb = float(request.form['Red blood cell distribution width'])
        mo = float(request.form['Monocytes'])
        wb = float(request.form['White blood cell count'])
        pcnt = float(request.form['Platelet Count'])
        lcnt = float(request.form['Lymphocyte Count'])
        ncnt = float(request.form['Neutrophils Count'])
        data = np.array([[age, gndr, antib, para, ox, vent, rb, mo, wb, pcnt, lcnt, ncnt]])

        #int_features = [float(data) for i in request.form.values()]  # Convert string inputs to float.
        #features = [np.array(int_features)]  # Convert to the form [[a, b]] for input to the model

        prediction = model.predict(data)  # features Must be in the form [[a, b]]
        print(prediction)
        # image=prediction[0]+'.png'
        #image=os.path.join(app.config['UPLOAD_FOLDER'],image)
        if prediction[0]==0 :
            x="Patient Is RECOVERED"
        else :
            x="Patient Is Not RECOVERED Yet !!! "

    return render_template('index.html',prediction=x)


if __name__ == '__main__':
    app.run(debug=True)