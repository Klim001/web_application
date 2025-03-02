def init_db(db_path):
    import sqlite3
    database = db_path
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            username TEXT NOT NULL,
            password TEXT NOT NULL
    )""")
    connection.commit()
    connection.close()

def save_to_db(dict, db_path):
    import sqlite3
    database = db_path
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO users (username, password) VALUES (?, ?)''', (
    dict['Имя'], dict['Пароль']))
    connection.commit()
    connection.close()

def right_entry(user, db_path):
    import sqlite3
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM users WHERE username = ?""", (user['Имя'],))
    usernames = cursor.fetchall()
    for i in usernames:
        if user['Пароль'] == i[1]:
            return 1
    return 0

def user_in_db(user, db_path):
    import sqlite3
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM users WHERE username = ?""", (user['Имя'],))
    usernames = cursor.fetchall()
    if len(usernames) > 0:
        return 1
    return 0

if __name__ == '__main__':
    init_db('users.db')
    user = {'Имя': 'gf', 'Пароль': 'dfghjk'}
    save_to_db(user, 'users.db')
    print(user_in_db(user, 'users.db'))
    print(right_entry(user, 'users.db'))
