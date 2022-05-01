import request
url='http://localhost:5000/predict_api'
r=requests.post(url,json={'Recency (months)':2,'Frequency (times)':50,'Monetary (c.c. blood)':12500,'Time (months)':98})

print(r.json())