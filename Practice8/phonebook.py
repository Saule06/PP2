from config import DATABASE
from connect import create_connection
def execute_query(query, params=None):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(query, params)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

# Function to return all records matching a pattern
def search_records(pattern):
    query = """
    SELECT * FROM contacts
    WHERE first_name ILIKE %s OR last_name ILIKE %s OR phone_number ILIKE %s;
    """
    params = (f"%{pattern}%", f"%{pattern}%", f"%{pattern}%")
    return execute_query(query, params)

# Procedure to insert a new user or update their phone number if they already exist
def insert_or_update_user(first_name, last_name, phone_number):
    query = """
    DO $$
    BEGIN
        IF EXISTS (SELECT 1 FROM contacts WHERE first_name = %s AND last_name = %s) THEN
            UPDATE contacts SET phone_number = %s WHERE first_name = %s AND last_name = %s;
        ELSE
            INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s);
        END IF;
    END $$;
    """
    params = (first_name, last_name, phone_number, first_name, last_name, first_name, last_name, phone_number)
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    cur.close()
    conn.close()

# Procedure to insert many users from a list with phone validation
def insert_many_users(users):
    invalid_users = []
    for user in users:
        first_name, last_name, phone_number = user
        if not validate_phone(phone_number):
            invalid_users.append(user)
        else:
            insert_or_update_user(first_name, last_name, phone_number)
    return invalid_users

# Function to validate phone number (basic validation)
def validate_phone(phone_number):
    return len(phone_number) == 10 and phone_number.isdigit()

# Function for pagination (limit and offset)
def query_data_with_pagination(limit, offset):
    query = """
    SELECT * FROM contacts
    LIMIT %s OFFSET %s;
    """
    params = (limit, offset)
    return execute_query(query, params)

# Procedure to delete data from the table by username or phone
def delete_user(identifier):
    query = """
    DELETE FROM contacts WHERE first_name = %s OR phone_number = %s;
    """
    params = (identifier, identifier)
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    cur.close()
    conn.close()

# Main function for testing
def main():
    # Example of searching records
    print("Search records:")
    print(search_records("John"))

    # Example of inserting or updating user
    insert_or_update_user("Jane", "Doe", "1234567890")

    # Example of inserting multiple users
    users_to_insert = [("Alice", "Smith", "2345678901"), ("Bob", "Brown", "3456789012")]
    print("Invalid users:", insert_many_users(users_to_insert))

    # Example of pagination
    print("Pagination result:")
    print(query_data_with_pagination(2, 0))

    # Example of deleting a user
    delete_user("Jane")

if __name__ == "__main__":
    main()