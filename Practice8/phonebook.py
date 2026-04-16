# phonebook.py

from connect import connect
import psycopg2


def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL UNIQUE
        );
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("Table checked/created.")


def run_sql_file(filename):
    conn = connect()
    cur = conn.cursor()

    with open(filename, "r", encoding="utf-8") as file:
        sql = file.read()
        cur.execute(sql)

    conn.commit()
    cur.close()
    conn.close()
    print(f"{filename} executed successfully.")


def search_by_pattern(pattern):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_phonebook(%s);", (pattern,))
    rows = cur.fetchall()

    print("\nSearch results:")
    for row in rows:
        print(row)

    cur.close()
    conn.close()


def get_paginated(limit, offset):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_phonebook_paginated(%s, %s);", (limit, offset))
    rows = cur.fetchall()

    print(f"\nPaginated results (LIMIT={limit}, OFFSET={offset}):")
    for row in rows:
        print(row)

    cur.close()
    conn.close()


def insert_or_update_user(name, phone):
    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL insert_or_update_user(%s, %s);", (name, phone))

    conn.commit()
    cur.close()
    conn.close()
    print(f"Inserted/updated user: {name}, {phone}")


def insert_many_users(names, phones):
    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL insert_many_users(%s, %s);", (names, phones))

    conn.commit()
    cur.close()
    conn.close()
    print("Many users inserted/updated.")


def delete_user(value):
    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL delete_user(%s);", (value,))

    conn.commit()
    cur.close()
    conn.close()
    print(f"Deleted by name or phone: {value}")


def show_all():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook ORDER BY id;")
    rows = cur.fetchall()

    print("\nAll records:")
    for row in rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    try:
        # 1. create table
        create_table()

        # 2. execute SQL files
        run_sql_file("functions.sql")
        run_sql_file("procedures.sql")

        # 3. insert/update one user
        insert_or_update_user("Alice", "87012345678")
        insert_or_update_user("Bob", "87098765432")
        insert_or_update_user("Alice", "87770001122")  # update

        # 4. insert many users
        names = ["Charlie", "David", "Eva", "Mira"]
        phones = ["87011111111", "123", "87022222222", "phone123"]  # some invalid
        insert_many_users(names, phones)

        # 5. show all
        show_all()

        # 6. search
        search_by_pattern("Ali")
        search_by_pattern("870")

        # 7. pagination
        get_paginated(2, 0)
        get_paginated(2, 2)

        # 8. delete
        delete_user("Bob")
        # delete_user("87022222222")

        # 9. show all again
        show_all()

    except Exception as e:
        print("Error:", e)