
import psycopg2



db_params = {
    'host': 'localhost',
    'dbname': 'userbase',
    'user': 'postgres_user',
    'password': 'postgres_password',
    'port': '5432',
}


conn = psycopg2.connect(**db_params)


cursor = conn.cursor()

query = "SELECT user_id,username,first_name,last_name FROM user_table WHERE username LIKE 'A%';"
cursor.execute(query)

results = cursor.fetchall()

conn.close()