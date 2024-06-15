CREATE OR REPLACE PROCEDURE udp_modify_account(
    IN address_street VARCHAR(30), 
    IN address_town VARCHAR(30)
)
AS
$$
DECLARE
    account_id INT;
    current_job_title VARCHAR(40);
BEGIN
    
    SELECT a.id, a.job_title 
    INTO account_id, current_job_title
    FROM accounts AS a
    JOIN addresses AS ad ON a.id = ad.account_id
    WHERE ad.street = address_street AND ad.town = address_town;

    
    IF FOUND THEN
        UPDATE accounts
        SET job_title = CONCAT('(Remote) ', current_job_title)
        WHERE id = account_id;
    END IF;
END;
$$
LANGUAGE plpgsql;
