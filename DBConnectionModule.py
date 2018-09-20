import sqlite3
from datetime import datetime




class DBConnection(object):
    def getBookInfo(ID,Authkey):
                #print(self)
                print(ID)
                print(Authkey)
                # SQLite DB 연결
                conn = sqlite3.connect("./simpleDB/simpledb.db")
                
                # Connection 으로부터 Cursor 생성
                cur = conn.cursor()
                
                # SQL 쿼리 실행
                query = "SELECT  eb.name , eb.ISBN , eb.forsale , "
                query+="eb.price FROM ebookInfo as eb left join userAndBook as ua on eb.no=ua.book_no "
                query+=" where ua.user_no = (select no from userInfo where id = '"+ ID+"' )"
                #+"' and valDate > '"+moment().format("YYYY-MM-DD")+"'"
                print(query)
                cur.execute(query)
                
                # 데이타 Fetch
                result=[]
                rows = cur.fetchall()
                for row in rows:
                    print(row[0], row[1])
                    result.append({"Name":row[0],"ISBN":row[1],"forsale":row[2],"price":row[3]})
                    #print(row[0])
                
                # Connection 닫기
                conn.close()

                print(rows.__len__)
                return result
    def validationAuthKey(ID,Authkey):
            # SQLite DB 연결
                conn = sqlite3.connect("./simpleDB/simpledb.db")
 
                #date=datetime.today().strftime("%Y-%m-%d%H%M%S")    # YYYYmmddHHMMSS 형태의 시간 출력
                date=datetime.today().strftime("%Y-%m-%d")
                print("date"+date)

                # Connection 으로부터 Cursor 생성
                cur = conn.cursor()
                
                # SQL 쿼리 실행
                query="SELECT  id, AuthKey FROM userInfo where id = '"+ID+"' and AuthKey = '"+Authkey+"'"
                query+=" and valDate > '"+date+"'"
                #+"' and valDate > '"+moment().format("YYYY-MM-DD")+"'"
                print(query)
                cur.execute(query)
                
                # 데이타 Fetch
                rows = cur.fetchall()
                for row in rows:
                    print(row[0], row[1])
                    #print(row[0])
                
                # Connection 닫기
                conn.close()
                print(len(rows))
                return len(rows)
                 