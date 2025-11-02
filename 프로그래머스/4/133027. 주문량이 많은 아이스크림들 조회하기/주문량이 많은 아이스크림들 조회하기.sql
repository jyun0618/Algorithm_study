WITH july_order AS (
    SELECT
        flavor,
        SUM(total_order) AS total_order
    FROM july
    GROUP BY flavor)
    
SELECT f.flavor
FROM first_half AS f
    LEFT JOIN july_order AS j
        ON f.flavor = j.flavor
ORDER BY f.total_order + j.total_order DESC
LIMIT 3