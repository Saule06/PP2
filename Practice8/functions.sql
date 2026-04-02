-- Function to search records matching a pattern
CREATE OR REPLACE FUNCTION search_records(pattern TEXT)
RETURNS TABLE(id INT, first_name VARCHAR, last_name VARCHAR, phone_number VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT id, first_name, last_name, phone_number
    FROM contacts
    WHERE first_name ILIKE '%' || pattern || '%'
       OR last_name ILIKE '%' || pattern || '%'
       OR phone_number ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- Function to validate phone number (basic validation)
CREATE OR REPLACE FUNCTION validate_phone(phone_number VARCHAR)
RETURNS BOOLEAN AS $$
BEGIN
    IF LENGTH(phone_number) = 10 AND phone_number ~ '^\d+$' THEN
        RETURN TRUE;
    ELSE
        RETURN FALSE;
    END IF;
END;
$$ LANGUAGE plpgsql;