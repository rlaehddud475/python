import mysql.connector
from getpass import getpass
passsword = getpass("MySQL root 비밀번호: ")
with mysql.connector.connect(
        host='127.0.0.1',   
        port=3306,                
        user='root',              
        password="1234",
        database='school_db',
        charset='utf8mb4',
)as connection:
    print("연결 성공")
    with connection.cursor() as cursor:
        cursor.execute("SELECT id,name,department FROM students ORDER BY id")
        for number, name, department in cursor:
            print(number, name, department,sep="\t")
    
