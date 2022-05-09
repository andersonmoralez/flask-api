from flask import Flask, jsonify
from flask_restx import Resource, Api

app = Flask('__name__')
api = Api(app)

@api.route('/home')
class HelloWorld(Resource):
    def get(self):
        return jsonify({'message':'Hello World!'})

if __name__ == '__main__':
    app.run(debug=True)
    

'''
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return {'message':'hello world!'}
'''