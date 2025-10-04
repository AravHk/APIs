from flask import Flask, request, jsonify
from flask_cors import CORS 
from datetime import datetime

app = Flask(__name__)
CORS(app)

events = []

@app.route('/')
def home():
    return jsonify({"message":"Aravindh is in his Prime"})

@app.route('/api/events',methods = ['POST'])
def create_event():
    data = request.get_json()
    event = {
        'id':len(events)+1,
        'title':data.get('title'),
        'duration':data.get('duration',60),
        'priority':data.get('deadline',''),
        'created_at':datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
    }
    events.append(event)
    return jsonify({'message':'Event created','event':event}),201

@app.route('/api/events',methods = ['GET'])
def get_events():
    return jsonify({'events':events,'count':len(events)})

if __name__ == '__main__':
    app.run(debug = True,port = 5000)

