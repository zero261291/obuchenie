import sqlite3
connection = sqlite3.connect('example.db')
connection.execute('''CREATE TABLE IF NOT EXISTS users
(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

def create_user(name, age):
    connection.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    connection.commit()

def read_user(id):
    cursor = connection.execute("SELECT * FROM users WHERE id=?", (id,))
    row = cursor.fetchone()
    return row

def update_user(id, name, age):
    connection.execute("UPDATE users SET name=?, age=? WHERE id=?", (name, age, id))
    connection.commit()

    connection.execute("DELETE FROM users WHERE id=?", (id,))
    connection.commit()

    create_user("John", 30)
    create_user("Jane", 25)

    user = read_user(1)
    print(user)

    update_user(1, "Johnny", 31)

    user = read_user(1)
    print(user)

    delete_user(1)

    user = read_u