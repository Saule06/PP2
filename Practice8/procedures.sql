-- Procedure to insert or update a user
CREATE OR REPLACE PROCEDURE insert_or_update_user(first_name TEXT, last_name TEXT, phone_number TEXT)
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE first_name = first_name AND last_name = last_name) THEN
        UPDATE contacts SET phone_number = phone_number WHERE first_name = first_name AND last_name = last_name;
    ELSE
        INSERT INTO contacts (first_name, last_name, phone_number) VALUES (first_name, last_name, phone_number);
    END IF;
END;
$$ LANGUAGE plpgsql;

-- Procedure to insert multiple users with phone validation
CREATE OR REPLACE PROCEDURE insert_many_users(users TEXT[])
AS $$
DECLARE
    user_record TEXT[];
    first_name TEXT;
    last_name TEXT;
    phone_number TEXT;
BEGIN
    FOREACH user_record IN ARRAY users LOOP
        first_name := user_record[1];
        last_name := user_record[2];
        phone_number := user_record[3];

        IF validate_phone(phone_number) THEN
            CALL insert_or_update_user(first_name, last_name, phone_number);
        ELSE
            RAISE NOTICE 'Invalid phone number for user % %: %', first_name, last_name, phone_number;
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

-- Procedure to delete a user by username or phone number
CREATE OR REPLACE PROCEDURE delete_user(identifier TEXT)
AS $$
BEGIN
    DELETE FROM contacts WHERE first_name = identifier OR phone_number = identifier;
END;
$$ LANGUAGE plpgsql;