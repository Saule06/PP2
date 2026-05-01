-- SEARCH FUNCTION
CREATE OR REPLACE FUNCTION search_contacts(q TEXT)
RETURNS TABLE(name VARCHAR, phone VARCHAR, email VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Ищет контакты по имени, email или телефону
    RETURN QUERY
    SELECT c.first_name, p.phone, c.email
    FROM contacts c
    LEFT JOIN phones p ON c.id = p.contact_id
    WHERE c.first_name ILIKE '%' || q || '%'
       OR c.email ILIKE '%' || q || '%'
       OR p.phone LIKE '%' || q || '%';
END;
$$;


-- UPSERT USER
CREATE OR REPLACE PROCEDURE upsert_user(
    p_first_name TEXT,
    p_last_name TEXT,
    p_phone TEXT
)
LANGUAGE plpgsql
AS $$
DECLARE
    cid INT;
BEGIN
    -- Ищем контакт по имени и фамилии
    SELECT id INTO cid
    FROM contacts
    WHERE first_name = p_first_name
      AND last_name = p_last_name;

    IF cid IS NULL THEN
        -- Если контакт не найден, создаём новый
        INSERT INTO contacts(first_name, last_name)
        VALUES (p_first_name, p_last_name)
        RETURNING id INTO cid;

        -- Добавляем телефон новому контакту
        INSERT INTO phones(contact_id, phone, type)
        VALUES (cid, p_phone, 'mobile');
    ELSE
        -- Если контакт найден, обновляем его телефон
        UPDATE phones
        SET phone = p_phone
        WHERE contact_id = cid;
    END IF;
END;
$$;


-- PAGINATION
CREATE OR REPLACE FUNCTION get_contacts(lim INT, off INT)
RETURNS TABLE(name VARCHAR, phone VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Возвращает контакты частями: LIMIT и OFFSET
    RETURN QUERY
    SELECT c.first_name, p.phone
    FROM contacts c
    JOIN phones p ON c.id = p.contact_id
    LIMIT lim OFFSET off;
END;
$$;


-- ADD PHONE
CREATE OR REPLACE PROCEDURE add_phone(
    p_name TEXT,
    p_phone TEXT,
    p_type TEXT
)
LANGUAGE plpgsql
AS $$
DECLARE
    cid INT;
BEGIN
    -- Ищем контакт по имени
    SELECT id INTO cid
    FROM contacts
    WHERE first_name = p_name;

    IF cid IS NULL THEN
        -- Если контакт не найден, выводим ошибку
        RAISE EXCEPTION 'Contact % not found', p_name;
    END IF;

    -- Добавляем новый телефон найденному контакту
    INSERT INTO phones(contact_id, phone, type)
    VALUES (cid, p_phone, p_type);
END;
$$;


-- MOVE TO GROUP
CREATE OR REPLACE PROCEDURE move_to_group(
    p_name TEXT,
    p_group TEXT
)
LANGUAGE plpgsql
AS $$
DECLARE
    gid INT;
    cid INT;
BEGIN
    -- Ищем группу
    SELECT id INTO gid
    FROM groups
    WHERE name = p_group;

    -- Если группы нет, создаём новую
    IF gid IS NULL THEN
        INSERT INTO groups(name)
        VALUES (p_group)
        RETURNING id INTO gid;
    END IF;

    -- Ищем контакт
    SELECT id INTO cid
    FROM contacts
    WHERE first_name = p_name;

    IF cid IS NULL THEN
        RAISE EXCEPTION 'Contact % not found', p_name;
    END IF;

    -- Перемещаем контакт в группу
    UPDATE contacts
    SET group_id = gid
    WHERE id = cid;
END;
$$;


-- DELETE CONTACT
CREATE OR REPLACE PROCEDURE delete_contact(
    p_query TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Удаляет контакт по имени или по номеру телефона
    DELETE FROM contacts
    WHERE first_name = p_query
       OR id IN (
           SELECT contact_id
           FROM phones
           WHERE phone = p_query
       );
END;
$$;


-- ВАЖНО:
-- Сначала удаляем старую процедуру, потому что PostgreSQL
-- не даёт менять имена параметров через CREATE OR REPLACE
DROP PROCEDURE IF EXISTS insert_many_users(TEXT[], TEXT[]);


-- INSERT MANY USERS
CREATE OR REPLACE PROCEDURE insert_many_users(
    p_names TEXT[],
    p_phones TEXT[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
    invalid_data TEXT[] := '{}';
BEGIN
    -- Проверяем, что длина массивов одинаковая
    IF array_length(p_names, 1) <> array_length(p_phones, 1) THEN
        RAISE EXCEPTION 'Names and phones arrays must have the same length';
    END IF;

    -- Проходимся по всем элементам массива
    FOR i IN 1..array_length(p_names, 1) LOOP

        -- Проверка телефона: только цифры и длина минимум 6
        IF p_phones[i] ~ '^[0-9]{6,}$' THEN

            -- Добавляем или обновляем пользователя
            -- Фамилию ставим пустой строкой, потому что в массиве есть только name
            CALL upsert_user(p_names[i], '', p_phones[i]);

        ELSE
            -- Если телефон неправильный, сохраняем его в invalid_data
            invalid_data := array_append(
                invalid_data,
                p_names[i] || ':' || p_phones[i]
            );
        END IF;

    END LOOP;

    -- Показываем неправильные данные
    RAISE NOTICE 'Invalid data: %', invalid_data;
END;
$$;


-- TEST EXAMPLES

-- Поиск контакта
SELECT * FROM search_contacts('Ali');

-- Добавить или обновить одного пользователя
CALL upsert_user('Mariya', 'Mamedova', '87071234567');

-- Получить контакты с пагинацией
SELECT * FROM get_contacts(5, 0);

-- Добавить второй номер контакту
CALL add_phone('Mariya', '87070000000', 'home');

-- Переместить контакт в группу
CALL move_to_group('Mariya', 'Friends');

-- Удалить контакт по имени или телефону
-- CALL delete_contact('Mariya');

