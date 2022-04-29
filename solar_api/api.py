from flask import Flask, request
import flasgger
from flasgger import Swagger
import pickle
import pandas as pd

api=Flask(__name__)
Swagger(api)

model=pickle.load(open('model.pkl', 'rb'))

@api.route('/')
def welcome():
  return 'Hello there!!!'

@api.route('/prediction', methods=['GET'])
def prediction():
  """Let's Predict the Solar State.
  ---
  parameters:
   - name: S1(Amp)
     in: query
     type: number
     required: true
   - name: S2(Amp)
     in: query
     type: number
     required: true
   - name: S1(Volt)
     in: query
     type: number
     required: true
   - name: S2(Volt)
     in: query
     type: number
     required: true
   - name: Light(kiloLux)
     in: query
     type: number
     required: true
   - name: Temp(degC)
     in: query
     type: number
     required: true
   - name: Weather
     in: query
     type: number
     required: true
  responses:
     200:
        description: The output values
  """

  s1_amp=request.args.get('S1(Amp)')
  s2_amp=request.args.get('S2(AMP)')
  s1_volt=request.args.get('S1(Volt)')
  s2_volt=request.args.get('S2(Volt)')
  light=request.args.get('Light(kiloLux)')
  temp=request.args.get('Temp(degC)')
  weather=request.args.get('Weather')

  prediction=model.predict([[s1_amp, s2_amp, s1_volt, s2_volt, light, temp, weather]])
  print(prediction)

  return "The Prediction is: "+prediction

@api.route('/predict_test_file', methods=['POST'])
def prediction_test_file():
  """Let's Predict the Whole Test Observations.
  ---
  parameters:
   - name: file
     in: formData
     type: file
     required: true
  responses:
     200:
          description: The output values
  """
  test_file=pd.read_csv(request.files.get('file'))
  print(test_file.head())
  prediction=model.predict(test_file)
  return str(list(prediction))

if __name__=='__main__':
  api.run()