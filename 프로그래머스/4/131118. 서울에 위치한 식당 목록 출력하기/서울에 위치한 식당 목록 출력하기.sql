# WITH review_avg AS (
#     SELECT 
#         rest_id,
#         ROUND(AVG(review_score), 2) AS score
#     FROM rest_review
#     GROUP BY 1
# )

SELECT 
    r1.rest_id,
    r1.rest_name,
    r1.food_type,
    r1.favorites,
    r1.address,
    ROUND(AVG(review_score), 2) AS score
FROM rest_info r1
    JOIN rest_review r2
        ON r1.rest_id = r2.rest_id
WHERE 1=1
    AND r1.address LIKE '서울%'
GROUP BY r1.rest_id
ORDER BY 6 DESC, 4 DESC