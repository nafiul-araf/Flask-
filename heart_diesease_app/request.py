import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'age_year':55, 'gender':0, 'ap_hi':120, 'ap_lo':80, 'cholesterol':1, 'gluc':0, 
                            'smoke':0, 'alco':1})

print(r.json())
