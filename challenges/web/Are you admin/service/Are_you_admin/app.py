import secrets
import sqlite3

from flask import Flask, request

app = Flask(__name__)

def get_db_connection():
    try:
        connection = sqlite3.connect(':memory:')
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        table_exists = cursor.fetchone()

        if not table_exists:
            create_table_query = """
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL
                )
            """
            cursor.execute(create_table_query)
            insert_query = """
                INSERT INTO users (username, password) VALUES (?, ?)
            """
            cursor.execute(insert_query, ('admin', secrets.token_hex(32)))
            connection.commit()
        cursor.close()

        return connection

    except Exception as e:
        print("Error connecting to the database:", str(e))
        return None


@app.route('/')
def home():
    return "Welcome to my Damn Vulnerable Web Application! Login with admin to the get the flag. You can find the login page in /login"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        connection = get_db_connection()
        cursor = connection.cursor()

        if username != 'admin':
            return "Invalid username, please try again!"
        
        cursor.execute(f"SELECT * FROM users WHERE username = 'admin' AND password = '{password}'")
        rows = cursor.fetchone()
        
        if rows:
            return 'Congratulations! You found the flag: YCEP24{Sql_Inj3ct1on_Is_V3ry_Cr1t1c4l}'
        else:
            return "Invalid password, please try again!"
    else:
        return '''
            <form method="post">
                Username: <input type="text" name="username"><br>
                Password: <input type="password" name="password"><br>
                <input type="submit" value="Login">
            </form>
            '''

if __name__ == '__main__':
    app.run("0.0.0.0", port=4000)
