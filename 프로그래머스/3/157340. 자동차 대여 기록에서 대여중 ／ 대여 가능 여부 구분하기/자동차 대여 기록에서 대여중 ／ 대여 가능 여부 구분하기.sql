WITH is_rental_tb AS (
    SELECT
        car_id,
        MAX(
            CASE
                WHEN start_date <= '2022-10-16' AND end_date >= '2022-10-16'
                    THEN 1
                ELSE 0
            END
        ) AS is_rental
    FROM car_rental_company_rental_history
GROUP BY car_id
)

SELECT
    car_id,
    CASE 
        when is_rental = 1 THEN '대여중'
        ELSE '대여 가능'
    END AS availability
FROM is_rental_tb
ORDER BY car_id DESC
