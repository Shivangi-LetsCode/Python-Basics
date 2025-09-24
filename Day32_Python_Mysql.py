'''
DATABASE:(sqlserver, mysql, sqlite, postgress, oracle, ...)
Database is a collection of Tables, Files, media etc..
CRUD : CREATE READ UPDATE DELETE

STEPS:
1) Download and install mysql
2) Download mysql python connector
3) pip install mysql-connector-python
'''
'''
#CONNECTION ESTABLISHMENT
import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',password='1234')
print(mydb.connection_id)
'''
'''
#CREATE DATABASE
import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',password='1234')
cursor = mydb.cursor()
cursor.execute("CREATE DATABASE pythonmysqlaag")
'''

'''
#CREATE TABLE
import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',password='1234',database='pythonmysqlaag')
cursor = mydb.cursor()
ct = ("CREATE TABLE customer(cust_id INT, FirstName VARCHAR(20),LastName VARCHAR(20),Age INT)")
cursor.execute(ct)'''

'''
#INSERT DATA
import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',password='1234',database='pythonmysqlaag')
cursor = mydb.cursor()
ct = "INSERT INTO customer VALUES(1,'John','Smith',23)"
cursor.execute(ct)
mydb.commit()'''

'''
#READ DATA
import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',password='1234',database='pythonmysqlaag')
cursor = mydb.cursor()
ct = "SELECT * FROM customer"
cursor.execute(ct)
result = cursor.fetchall()
print(result)'''

'''
#UPDATE DATA
import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',password='1234',database='pythonmysqlaag')
cursor = mydb.cursor()
ct = "UPDATE customer SET Age = 19 WHERE cust_id = 1"
cursor.execute(ct)
mydb.commit()'''

'''
import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',password='1234',database='pythonmysqlaag')
cursor = mydb.cursor()
ct = "DELETE FROM customer WHERE cust_id = 1"
cursor.execute(ct)
mydb.commit()'''





























