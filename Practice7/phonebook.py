

import csv
import psycopg2
from connect import create_connection


def insert_contact(first_name, last_name, phone_number):
    conn = create_connection()
    cur = conn.cursor()
    
    cur.execute("""
        INSERT INTO contacts (first_name, last_name, phone_number) 
        VALUES (%s, %s, %s)
    """, (first_name, last_name, phone_number))
    
    conn.commit()
    cur.close()
    conn.close()


def insert_from_csv(csv_file):
    conn = create_connection()
    cur = conn.cursor()
    
    with open(csv_file, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            first_name, last_name, phone_number = row
            cur.execute("""
                INSERT INTO contacts (first_name, last_name, phone_number)
                VALUES (%s, %s, %s)
            """, (first_name, last_name, phone_number))
    
    conn.commit()
    cur.close()
    conn.close()


def update_contact(phone_number, new_first_name=None, new_phone_number=None):
    conn = create_connection()
    cur = conn.cursor()

    if new_first_name:
        cur.execute("""
            UPDATE contacts
            SET first_name = %s
            WHERE phone_number = %s
        """, (new_first_name, phone_number))

    if new_phone_number:
        cur.execute("""
            UPDATE contacts
            SET phone_number = %s
            WHERE phone_number = %s
        """, (new_phone_number, phone_number))

    conn.commit()
    cur.close()
    conn.close()


def query_contacts(filter_type, filter_value):
    conn = create_connection()
    cur = conn.cursor()

    if filter_type == 'name':
        cur.execute("""
            SELECT * FROM contacts WHERE first_name LIKE %s OR last_name LIKE %s
        """, (f'%{filter_value}%', f'%{filter_value}%'))
    elif filter_type == 'phone':
        cur.execute("""
            SELECT * FROM contacts WHERE phone_number LIKE %s
        """, (f'{filter_value}%',))
    
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    cur.close()
    conn.close()


def delete_contact(phone_number):
    conn = create_connection()
    cur = conn.cursor()
    
    cur.execute("""
        DELETE FROM contacts WHERE phone_number = %s
    """, (phone_number,))
    
    conn.commit()
    cur.close()
    conn.close()


def main():
    # Insert contacts entered from the console
    while True:
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone_number = input("Enter phone number: ")
        insert_contact(first_name, last_name, phone_number)

        more = input("Do you want to add another contact? (y/n): ")
        if more.lower() != 'y':
            break
    
    # Insert from CSV
    csv_file = input("Enter CSV file name to import data: ")
    insert_from_csv(csv_file)

    # Update contact details
    phone_number = input("Enter phone number to update: ")
    new_first_name = input("Enter new first name (leave blank to keep unchanged): ")
    new_phone_number = input("Enter new phone number (leave blank to keep unchanged): ")
    update_contact(phone_number, new_first_name, new_phone_number)

    # Query contacts
    filter_type = input("Filter by (name/phone): ")
    filter_value = input("Enter filter value: ")
    query_contacts(filter_type, filter_value)

    # Delete contact
    phone_number = input("Enter phone number to delete: ")
    delete_contact(phone_number)

if __name__ == "__main__":
    main()