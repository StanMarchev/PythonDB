SELECT
    name,
    at.animal_type,
    to_char(a.birthdate, 'DD.MM.YYYY') as birthday

FROM animals as a
    join animal_types as at
        on a.animal_type_id = at.id

ORDER BY name