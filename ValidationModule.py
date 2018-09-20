import DBConnectionModule

class ValidationProcess():
    def forIDandKey(self,ID,Authkey):
        dbConnection=DBConnectionModule.DBConnection
        count=dbConnection.validationAuthKey(ID,Authkey)
        #count=dbConnection.getBookInfo(ID,Authkey)
        if count==1:
            return True
        
        else:
            return False
        
        #return True