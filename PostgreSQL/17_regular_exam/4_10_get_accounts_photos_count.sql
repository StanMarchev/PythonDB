CREATE OR REPLACE FUNCTION udf_accounts_photos_count(account_username VARCHAR(30)) 
RETURNS INT AS
    $$
    DECLARE
        photos_count INT;
    BEGIN
        SELECT
            count(*)
        INTO photos_count
        FROM accounts_photos as ap
        JOIN accounts as a
        ON ap.account_id = a.id
        WHERE a.username = account_username;
        RETURN photos_count;
    END;
$$
LANGUAGE plpgsql;
