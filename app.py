from flask import Flask ,Response,request
#from flask_restful import Resource, Api
import ValidationModule
import DBConnectionModule
import json
app = Flask(__name__)
#app.run(host='0.0.0.0', port=8787, debug=True) 

@app.route("/getBookInfo",methods=["PUT"])
def getBookInfo():
    
    #result={"code":200,"message":"Respond Success","data":None}
    print(request.json)
    print(request.json['ID'])
    validation=ValidationModule.ValidationProcess()
    if validation.forIDandKey(request.json['ID'],request.json['APIKey'])==True:
        bookInfo=DBConnectionModule.DBConnection.getBookInfo(request.json['ID'],request.json['APIKey'])

        result= {'code':200,'message':'Respond Success','data':bookInfo}
        
    else:
        result= {'code':403,'message':'Invalid Auth key or Expire key','data':None}

    resp = Response(json.dumps(result))
    #resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Content-Type'] = 'application/json'
    return resp
    #Respond.
    #return json.dumps(result)



if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5009)
    # TODO 나중에 포트 변경에 대해서 확인 후 변경해 두기 
    # 위의 debug=True,host="0.0.0.0",port=5009 부분도 안먹음..
    # 무조건 5000 에 debug false 로 실행 됨... 이유가 뭐지..
    #app.run(host='0.0.0.0', port=8787, debug=True) 
