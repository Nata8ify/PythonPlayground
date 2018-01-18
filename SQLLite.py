import os

import sqlite3


def Main():
    db_name = "pgim.txt"
    print(os.getcwd())
    is_existed = os.path.exists(db_name)
    conn = sqlite3.connect(db_name)
    if not is_existed :
        conn.executescript("CREATE TABLE sample("
                           "id integer primary key autoincrement not null,"
                           "name text not null,"
                           "write_date date not null);")
        conn.execute("INSERT INTO sample (id, name, write_date) VALUES (1, 'Nattawut', date('now'));")
        conn.execute("INSERT INTO sample (id, name, write_date) VALUES (2, 'Ferry Tubby', date('now'));")
        conn.execute("INSERT INTO sample (id, name, write_date) VALUES (3, 'Dale Niggel', date('now'));")
        conn.execute("INSERT INTO sample (id, name, write_date) VALUES (4, 'Lombo Koko', date('now'));")
        conn.execute("INSERT INTO sample (id, name, write_date) VALUES (5, 'Bal Lad', date('now'));")
        conn.commit()

    result_set = conn.execute("SELECT * FROM sample;")
    for row in result_set.fetchall():
        print("-> "+str(row))

    conn.close()

if __name__ == "__main__" :
    Main()