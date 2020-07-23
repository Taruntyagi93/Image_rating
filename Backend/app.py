from flask import Flask, request, Response, make_response, jsonify
from database.db import initialize_db
from database.models import Counter
from flask_cors import CORS

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://test:test1234@ds229295.mlab.com:29295/movie-bag?retryWrites=false'
}

CORS(app)

db = initialize_db(app)


@app.route('/counter')
def get_counters():
    print(Counter)
    counter = Counter.objects().all().to_json()
    print(counter)
    return Response(counter, mimetype="application/json", status=200)


@app.route('/updateCounter', methods=['POST'])
def update_counter():
    input = request.get_json()
    for curr in input:
        Counter.objects(name=curr['name']).update(set__counter=curr['counter'])
    return make_response(jsonify({"success": True, "data": 1}), 200)


app.run()
