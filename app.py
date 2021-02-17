from flask import Flask, request, jsonify
from flask_cors import CORS
import turicreate as tc

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    
    data = tc.SFrame({'user_id': ["Ann", "Ann", "Ann", "Brian", "Brian", "Brian"],
                          'item_id': ["Item1", "Item2", "Item4", "Item2", "Item3", "Item5"],
                          'rating': [1, 3, 2, 5, 4, 2]})
    m = tc.factorization_recommender.create(data, target='rating')

    recommendations = m.recommend()
    return(recommendations)
