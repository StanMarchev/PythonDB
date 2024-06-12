SELECT
    name AS animial,
    EXTRACT('year' FROM birthdate) as birth_year,
    at.animal_type
FROM animals as a
        JOIN animal_types as at
            on a.animal_type_id = at.id

WHERE
    at.animal_type <> 'Birds'
    and age('01/01/2022', a.birthdate ) < '5 year'
    and a.owner_id is NULL

ORDER BY a.name
