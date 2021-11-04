-- Cities by State (join)
-- List all cities (and their state) from hlbtn_0d_usa database
SELECT cities.id, cities.name, states.name
FROM cities LEFT JOIN states
    ON cities.state_id = states.id
ORDER BY cities.id ASC;