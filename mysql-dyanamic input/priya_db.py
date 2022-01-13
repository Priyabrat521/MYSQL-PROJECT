import pymysql

con=pymysql.connect(host='localhost',user='root',password='12345',database='priyadb')
cursor=con.cursor()
#CREATE DATABASE
# cursor.execute('CREATE DATABASE priyadb')
#CREATE STUDENT TABLE
# cursor.execute('CREATE TABLE student_data(sname varchar(30),sid int(10),saddress varchar(100))')
#TAKE INPUTS FROM USER
while True:
    sname=input('ENTER STUDENT NAME:')
    sid=int(input('ENTER STUDENT ID:'))
    saddress=input('ENTER STUDNT ADDRESS:')
    query='INSERT INTO student_data (sname,sid,saddress) VALUES(%s,%s,%s)'
    values=(sname,sid,saddress)
    cursor.execute(query,values)
    con.commit()
    print('THANK YOU !!!YOUR DATA SAVED')
    option=input('DO YOU WANT TO ADD ONE MORE VALUE: [YES|NO]:')
    if option.lower()=='no':
        break
    
