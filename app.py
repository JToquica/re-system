from flask import Flask
from flask_cors import CORS
import turicreate as tc

app = Flask(__name__)
CORS(app)

@app.route('/recomendaciones', methods=['POST'])
def hello_world_json_list():

        json_data = request.json

        calificacion = {'user_id': ["Ann", "Ann", "Ann", "Brian", "Brian", "Brian"],
                        'item_id': ["Item1", "Item2", "Item4", "Item2", "Item3", "Item5"],
                        'rating': [1, 3, 2, 5, 4, 2]}

        data = tc.SFrame(calificacion)

        m = tc.factorization_recommender.create(data, target='rating')

        recommendations = m.recommend(users=['Brian'])

        datos = []

        for i in recommendations:
                datos.append(i)

        #return {"data":datos}
        return {"data":json_data}
    
    

if __name__ == '__main__':
    app.run
