import pickle
import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from URLFeatureExtraction import featureExtraction

filename = 'Phishing-detector-xgboost-model.pkl'
xgb = pickle.load(open(filename, 'rb'))


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        url = request.form['url']
        
        sample = pd.DataFrame(np.array([[int(x) for x in featureExtraction(url)]]))
        prediction=xgb.predict(sample)
        if  prediction[0] == 1:
            result='Phishing'
        elif  prediction[0] == 0:
            result = 'Legit'
        return render_template('prediction_page.html',type = result)
    else: 
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
