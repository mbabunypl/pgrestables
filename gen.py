
import random
import json
import time
import psycopg2
from psycopg2 import sql

# List of 20 common first names
first_names = [
    "Emma", "Liam", "Olivia", "Noah", "Ava", 
    "Isabella", "Sophia", "Jackson", "Lucas", "Aiden", 
    "Mia", "Elijah", "Grayson", "Harper", "Evelyn", 
    "Abigail", "Amelia", "Benjamin", "Ethan", "Mason",
    "Sofía", "Mateo", "Valentina", "Emiliano", "Regina",
    "Ximena", "Sebastián", "Mariana", "Leonardo", "Renata",
    "Victoria", "Diego", "Camila", "Joaquín", "Fernanda",
    "Isabella", "Luis", "Sara", "Alejandro", "Adriana",
    "Emma", "Liam", "Olivia", "Noah", "Sophia",
    "Ethan", "Ava", "Lucas", "Isabella", "Jackson",
    "Charlotte", "Liam", "Amelia", "Benjamin", "Mia",
    "William", "Abigail", "James", "Ella", "Sophie",
    "Wei", "Xia", "Chen", "Yun", "Yong",
    "Li", "Fang", "Zhang", "Xin", "Jing",
    "Ming", "Ling", "Jun", "Hui", "Qing",
    "Xiu", "Yan", "Tao", "Xiang", "Yu"
]

# List of 20 common last names
last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", 
    "García", "Miller", "Davis", "Rodriguez", "Martínez", 
    "Hernández", "López", "González", "Perez", "Wilson", 
    "Walker", "Moore", "Taylor", "Jackson", "White",
    "Hernández", "Gómez", "García", "Martínez", "López",
    "Pérez", "González", "Rodríguez", "Fernández", "Sánchez",
    "Ramírez", "Torres", "Díaz", "Vázquez", "Castro",
    "Ruiz", "Jiménez", "Moreno", "Ramos", "Rojas",
     "Smith", "Johnson", "Brown", "Li", "Patel",
    "Garcia", "Martinez", "Taylor", "White", "Harris",
    "Anderson", "Thomas", "Jackson", "Clark", "Lee",
    "Walker", "Hall", "Young", "Wright", "King",
    "Li", "Wang", "Zhang", "Liu", "Chen",
    "Yang", "Huang", "Zhao", "Zhou", "Wu",
    "Xu", "Sun", "Ma", "Hu", "Zhu",
    "Guo", "Lin", "He", "Gao", "Lu"
    
    
]


# List of common first names in India
first_names.extend([
    "Aarav", "Sanya", "Arjun", "Divya", "Rahul",
    "Aisha", "Vikram", "Priya", "Aditya", "Ananya",
    "Rohan", "Ishaan", "Sneha", "Karthik", "Neha",
    "Kabir", "Pooja", "Raj", "Swati", "Harsh"
])

# List of common last names in India
last_names.extend( [
    "Sharma", "Patel", "Kumar", "Singh", "Gupta",
    "Shah", "Malhotra", "Chauhan", "Verma", "Reddy",
    "Sinha", "Jain", "Das", "Mukherjee", "Rao",
    "Roy", "Yadav", "Mehta", "Pandey", "Thakur"
])


# List of common first names in Indonesia
first_names.extend([
    "Putu", "Made", "Nyoman", "Ketut", "I Wayan",
    "I Made", "I Nyoman", "I Ketut", "Agus", "Budi",
    "Dewi", "Sri", "Siti", "Anita", "Hadi",
    "Eko", "Surya", "Dian", "Tri", "Nur"
])

# List of common last names in Indonesia
last_names.extend( [
    "Suryanto", "Hartono", "Wijaya", "Saputra", "Wijaya",
    "Sari", "Ningsih", "Setiawan", "Purnama", "Susanto",
    "Kusuma", "Lestari", "Rahayu", "Santoso", "Pratama",
    "Putra", "Utama", "Wahyuni", "Mulyani", "Hadi"
])


first_names.extend([
    "Muhammad", "Aisha", "Ali", "Fatima", "Ahmed",
    "Sana", "Faisal", "Zainab", "Hassan", "Ayesha",
    "Omar", "Zoya", "Bilal", "Hira", "Imran",
    "Amina", "Sajid", "Nadia", "Usman", "Samina"
])

# List of common last names in Pakistan
last_names.extend(  [
    "Khan", "Abbasi", "Raza", "Malik", "Shah",
    "Hussain", "Ali", "Ahmed", "Iqbal", "Siddiqui",
    "Rehman", "Qureshi", "Akhtar", "Nawaz", "Rafiq",
    "Farooq", "Begum", "Arif", "Zafar", "Aslam"
])

# List of common first names in Brazil
first_names.extend([
    "Ana", "Lucas", "Maria", "Pedro", "Isabela",
    "Matheus", "Julia", "Gabriel", "Larissa", "Bruno",
    "Camila", "Diego", "Bianca", "Felipe", "Amanda",
    "Rafael", "Mariana", "Vinícius", "Fernanda", "Thiago"
])

# List of common last names in Brazil
last_names.extend(  [
    "Silva", "Santos", "Oliveira", "Souza", "Rodrigues",
    "Lima", "Pereira", "Carvalho", "Costa", "Martins",
    "Ferreira", "Almeida", "Nascimento", "Araújo", "Melo",
    "Cavalcanti", "Cardoso", "Gomes", "Teixeira", "Ribeiro"
])

first_names.extend([
    "Chijioke", "Fatima", "Oluwakemi", "Abdul", "Ngozi",
    "Chinedu", "Aisha", "Olumide", "Chiamaka", "Mohammed",
    "Chinwe", "Adeola", "Jibril", "Nneka", "Ibrahim",
    "Chidinma", "Oluwaseun", "Obinna", "Aminat", "Emeka"
])

# List of common last names in Nigeria
last_names.extend(  [
    "Adeyemi", "Okafor", "Ogunjimi", "Adeleke", "Eze",
    "Oluwole", "Adegoke", "Ibrahim", "Nwosu", "Okafor",
    "Adeyinka", "Olatunji", "Onwuka", "Nwachukwu", "Ogunleye",
    "Ejiofor", "Adewale", "Obi", "Abubakar", "Afolayan"
])




# List of common first names in Bangladesh
first_names.extend([
    "Mohammed", "Fatima", "Aminul", "Sadia", "Rahman",
    "Aisha", "Nur", "Fahim", "Tahmina", "Kabir",
    "Nusrat", "Mehedi", "Farida", "Imran", "Moushumi",
    "Riaz", "Shabnam", "Kamal", "Tasnim", "Rubi"
])

# List of common last names in Bangladesh
last_names.extend([
    "Rahman", "Khan", "Hossain", "Ahmed", "Ali",
    "Chowdhury", "Islam", "Khatun", "Akter", "Haque",
    "Miah", "Choudhury", "Das", "Uddin", "Begum",
    "Siddique", "Hossain", "Karim", "Yasmin", "Kabir"
])



# List of common first names in Russia
first_names.extend([
    "Alexander", "Maria", "Dmitry", "Ekaterina", "Sergei",
    "Olga", "Ivan", "Natalia", "Vladimir", "Anna",
    "Mikhail", "Elena", "Maxim", "Irina", "Andrey",
    "Tatiana", "Artem", "Yulia", "Nikolai", "Anastasia"
])

# List of common last names in Russia
last_names.extend( [
    "Ivanov", "Smirnov", "Kuznetsov", "Popov", "Vasilyev",
    "Petrov", "Sokolov", "Mikhailov", "Novikov", "Fedorov",
    "Morozov", "Andreev", "Bogdanov", "Volkov", "Solovyov",
    "Kozlov", "Orlov", "Lebedev", "Egorov", "Stepanova"
])





x = random.randint(0,len(first_names)-1)


def create_row():
    x = random.choice(first_names)
    y = random.choice(last_names)
    return {
        'username' : f"{x[0] + y}",
        'first_name' : x,
        'last_name' : y,
        'user_id' : random.randint(10**10,10**11-1)
        
    }



import psycopg2
from psycopg2 import sql
import random
import time

# Function to create a user table
def create_user_table(cursor):
    create_table_query = """
        CREATE TABLE IF NOT EXISTS user_table (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(255),
            first_name VARCHAR(255),
            last_name VARCHAR(255)
        );
    """
    cursor.execute(create_table_query)

# Function to insert a user into the user table
def insert_user(cursor, username, first_name, last_name):
    insert_query = sql.SQL("""
        INSERT INTO user_table (username, first_name, last_name)
        VALUES (%s, %s, %s)
        RETURNING user_id;
    """)
    cursor.execute(insert_query, (username, first_name, last_name))
    user_id = cursor.fetchone()[0]
    return user_id

# Connection parameters
db_params = {
    'host': "127.0.0.1",
    'dbname': 'userbase',
    'user': 'postgres_user',
    'password': 'postgres_password',
    'port': 5432,
}
conn = None 
try:
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(**db_params)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Create the user table
    create_user_table(cursor)

    # Insert a new user every 5 seconds
    while True:
        user_data = create_row()
        user_id = insert_user(cursor, user_data['username'], user_data['first_name'], user_data['last_name'])
        conn.commit()
        print(f'User inserted with ID: {user_id}')
        time.sleep(1)

except Exception as e:
    print(f"Error: {e}")

finally:
    if conn:
        conn.close()
