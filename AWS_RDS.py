import MySQLdb

class AWS:
    # 以MySQL登入AWS RDS並創建資料表 shops、products、Images
    def __init__(self):
        host = "rds-mysql-rex.cscjvvfseets.us-east-1.rds.amazonaws.com"
        passwd = str(input("PASSWORD : "))
        conn = MySQLdb.connect(host, port=3306, user='rex', passwd=passwd, db="NBA")
        cur = conn.cursor()
            
        sql = "CREATE TABLE NBA.news (id INT PRIMARY KEY, title VARCHAR(255), content TEXT, time VARCHAR(50))"
        cur.execute(sql)
        conn.commit()
        
        sql = "CREATE TABLE NBA.image (id INT, image VARCHAR(255), FOREIGN KEY (id) REFERENCES news (id));"
        cur.execute(sql)
        conn.commit()
        
        conn.close()
        

if __name__ == "__main__":
    
    AWS_database = AWS()