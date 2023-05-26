-- Lists all cities in the 'hbtn_0d_usa' database that belong to California.
-- Results are ordered by ascending 'cities.id'.

SELECT c.id, c.name
FROM cities AS c
WHERE c.state_id IN (
    SELECT s.id
    FROM states AS s
    WHERE s.name = 'California'
)
ORDER BY c.id;
