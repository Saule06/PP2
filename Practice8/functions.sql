
-- functions.sql

-- Если таблицы еще нет, можно создать так:
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL UNIQUE
);

-- 1) Function: search records by pattern
-- Ищет совпадение в имени или телефоне
CREATE OR REPLACE FUNCTION search_phonebook(pattern_text TEXT)
RETURNS TABLE (
    id INTEGER,
    first_name VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.first_name, p.phone
    FROM phonebook p
    WHERE p.first_name ILIKE '%' || pattern_text || '%'
       OR p.phone ILIKE '%' || pattern_text || '%';
END;
$$ LANGUAGE plpgsql;


-- 2) Function: get data with pagination
CREATE OR REPLACE FUNCTION get_phonebook_paginated(p_limit INTEGER, p_offset INTEGER)
RETURNS TABLE (
    id INTEGER,
    first_name VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT pb.id, pb.first_name, pb.phone
    FROM phonebook pb
    ORDER BY pb.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;