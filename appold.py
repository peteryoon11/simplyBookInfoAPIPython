from flask import Flask
from flask_restful import Resource, Api
import ValidationModule

app = Flask(__name__)
#app.run(host='0.0.0.0', port=8787, debug=True) 

api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    def put(self):
        validation=ValidationModule.ValidationProcess()
        if validation.forIDandKey()==True:
            return {'code':200,'message':'Respond Success','data':None}
        
        else:
            return {'code':403,'message':'Invalid Auth key or Expire key','data':None}

            
        
        








api.add_resource(HelloWorld, '/getBookInfo')

if __name__ == '__main__':
    app.run(debug=True)
    # TODO 나중에 포트 변경에 대해서 확인 후 변경해 두기 
    #app.run(host='0.0.0.0', port=8787, debug=True) 
