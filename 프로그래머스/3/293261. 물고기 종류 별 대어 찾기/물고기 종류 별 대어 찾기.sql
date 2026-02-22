WITH big_fish AS (
    SELECT
        fish_type,
        MAX(length) AS length
    FROM fish_info
    GROUP BY fish_type 
)

SELECT
    fi.id,
    fni.fish_name,
    fi.length
FROM fish_info AS fi
    JOIN big_fish AS bf
        ON fi.fish_type = bf.fish_type
            AND fi.length = bf.length
    JOIN fish_name_info AS fni
        ON fi.fish_type = fni.fish_type
ORDER BY fi.id