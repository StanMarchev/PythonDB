SELECT
    v.name AS volunteers,
    v.phone_number,
    substring(trim(replace(v.address, 'Sofia', '')),3) as address
FROM volunteers as v
        JOIN volunteers_departments as vd
            ON v.department_id = vd.id

WHERE
    vd.department_name = 'Education program assistant'
    and v.address LIKE '%Sofia%'
ORDER BY v.name