
import mysql.connector
conn = mysql.connector.connect(user = "root", password ="", host = "localhost", database = "springboot")
def Main():
    query()
    #insert()

def query():
    cursor = conn.cursor()
    sql = "SELECT * FROM users WHERE id BETWEEN %s AND %s;"
    cursor.execute(operation = sql, params = (1, 100))
    for (i, j, u) in cursor: # parameters i, j and u store result by column id, email and password ordered.
        print(str(i)+" : "+j+" : "+u)

def insert():
    cursor = conn.cursor()
    sql = "INSERT INTO users (email, password) VALUES (%(email)s, %(password)s);"
    data = {
        'email' : input("Enter an E-mail : "),
        'password' : input("Enter a Password : ")
    }
    cursor.execute(operation= sql , params= data)


def close():
    conn.close

if __name__ == "__main__":
    Main()