SELECT
    c.full_name,
    COUNT(cr.car_id) AS count_of_cars,
    SUM(cr.bill) AS total_sum
FROM clients as c
        JOIN courses as cr
            ON c.id = cr.client_id
WHERE 
	SUBSTRING(c.full_name, 2, 1) = 'a' 

GROUP BY c.full_name

HAVING 
    COUNT(car_id) > 1

ORDER BY c.full_name;