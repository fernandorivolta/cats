from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
import pymongo
from bson.json_util import dumps

app = Flask(__name__)
metrics = PrometheusMetrics(app)
client = pymongo.MongoClient("mongodb://mongo:27017/")
mydb = client["db"]
col_breeds = mydb["breeds"]

@app.route('/breeds')
def breeds():
    return { 
        'breeds' : col_breeds.distinct('breed')
    }

@app.route('/breed/<filter>')
def breed(filter):
    print(filter)
    return dumps(col_breeds.find_one({'breed' : filter}, {'_id': False}))

@app.route('/breeds/temperament/<filter>')
def breeds_temperament(filter):
    breeds = []
    for x in col_breeds.find({'temperament' : filter}, {'_id': False}):
        if x['breed'] not in breeds:
            breeds.append(x['breed'])
    return dumps(breeds)

@app.route('/breeds/origin/<filter>')
def breeds_origin(filter):
    breeds = []
    for x in col_breeds.find({'origin' : filter}, {'_id': False}):
        if x['breed'] not in breeds:
            breeds.append(x['breed'])
    return dumps(breeds)

app.run(host='0.0.0.0', port=80)