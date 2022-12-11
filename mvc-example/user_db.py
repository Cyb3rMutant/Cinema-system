from DataAccessObject import * 
c = conn.cursor()
c.execute('''
DROP TABLE if exists users
''')
c.execute('''
DROP TABLE if exists user
''')
c.execute('''
CREATE TABLE users
(username varchar(20) PRIMARY KEY, password varchar(20) NOT NULL)
''')

#c.commit()
#conn.close()