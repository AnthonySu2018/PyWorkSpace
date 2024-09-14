import pymysql

def connect():
    # Establish a connection to the MySQL database
    connection = pymysql.connect(
        host='127.0.0.1',
        port=3308,
        user='root',
        password='Admin@168',
        database='classicmodels'
    )
    print("Connected to the database")
    return connection

def select(query):
    # Execute a SELECT query and return the results
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    print(results)
    connection.close()
    return results

def update(query):
    # Execute an UPDATE query
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def delete(query):
    # Execute a DELETE query
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

def insert(query):
    # Execute an INSERT query
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()


select('select * from employees where employeeNumber =1002')