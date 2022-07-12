import psycopg2
from psycopg2 import extras

## CRUD CON POSTGRES
host = "tus datos"
database = "tus datos"
user = "tus datos"
password = "tus datos"
port =  5432

cur = None
try: 
    conn = psycopg2.connect(
    host = host,
    database = database,
    user = user,
    password =  password,
    port = port
    
)
    cur =  conn.cursor(cursor_factory=extras.RealDictCursor)
    
   ## cur.execute("""CREATE TABLE IF NOT 
   ## EXISTS users(
   ## id SERIAL PRIMARY KEY,
   ## name VARCHAR(255) NOT NULL,
   ## email VARCHAR(255) NOT NULL,
   ## password VARCHAR(255) NOT NULL
   ## )
    
  ##  """);
   ## const_insert = ##('daniel','daniel@gmail.com','defdfgt')
   ## conn_query = "INSERT INTO users(name, ##email, password) VALUES(%s,%s,%s)"
  ##  cur.execute(conn_query, const_insert)
   ## cur.execute("SELECT *  FROM users")
    ## for row in cur.fetchall():
       ## print(row)
    delete = "DELETE FROM users WHERE id = %s RETURNING *"
    deleteData= "2"
    cur.execute(delete, deleteData)
    user = cur.fetchone()
    conn.commit()
    print(user)
    
 
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()

