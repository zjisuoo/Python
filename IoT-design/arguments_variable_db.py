def connect(**options) :
    conn_params = {
        'host' : options.get('host', '127.0.0.1'),
        'port' : options.get('post', 5432),
        'user' : option.get('user', ''),
        'pwd' : options.get('pwd', ''),
    }
    print(conn_params)
# we then connect to the db (commented out)
# db.connect(**conn_params)

connect()
connect(host = '127.0.0.42', port = 5433)
connect(port = 5431, useer = 'fab', pwd = 'gandalf')