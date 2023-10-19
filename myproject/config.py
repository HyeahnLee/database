db = {
    'user': 'root',
    'password': '[2021011545]',
    'host': '127.0.0.1',
    'port': '3306',
    'database': 'news'
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"