CREATE OR REPLACE PROCEDURE sp_animals_with_owners_or_not(
    IN animal_name varchar(30),
    OUT result varchar(30)
)

AS
$$

    BEGIN
        SELECT
            o.name
        INTO result
        FROM owners as o
            JOIN animals as a
                ON o.id = a.owner_id
        WHERE a.name = animal_name;

        if result is NULL then result := 'For adoption'; end if;
    END;
$$
LANGUAGE plpgsql;


