
-- procedures.sql

-- 1) Procedure: insert new user or update phone if user already exists
CREATE OR REPLACE PROCEDURE insert_or_update_user(p_name TEXT, p_phone TEXT)
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = p_name) THEN
        UPDATE phonebook
        SET phone = p_phone
        WHERE first_name = p_name;
    ELSE
        INSERT INTO phonebook(first_name, phone)
        VALUES (p_name, p_phone);
    END IF;
END;
$$ LANGUAGE plpgsql;


-- 2) Procedure: insert many users with validation
-- Проверка телефона: только цифры, длина от 10 до 15
-- Некорректные данные выводим через NOTICE
CREATE OR REPLACE PROCEDURE insert_many_users(
    p_names TEXT[],
    p_phones TEXT[]
)
AS $$
DECLARE
    i INTEGER;
    current_name TEXT;
    current_phone TEXT;
BEGIN
    IF array_length(p_names, 1) IS DISTINCT FROM array_length(p_phones, 1) THEN
        RAISE EXCEPTION 'Names and phones arrays must have the same length';
    END IF;

    FOR i IN 1..array_length(p_names, 1) LOOP
        current_name := p_names[i];
        current_phone := p_phones[i];

        -- validate phone
        IF current_phone ~ '^[0-9]{10,15}$' THEN
            IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = current_name) THEN
                UPDATE phonebook
                SET phone = current_phone
                WHERE first_name = current_name;
            ELSE
                INSERT INTO phonebook(first_name, phone)
                VALUES (current_name, current_phone);
            END IF;
        ELSE
            RAISE NOTICE 'Incorrect data: name = %, phone = %', current_name, current_phone;
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;


-- 3) Procedure: delete by username or phone
CREATE OR REPLACE PROCEDURE delete_user(p_value TEXT)
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE first_name = p_value
       OR phone = p_value;
END;
$$ LANGUAGE plpgsql;