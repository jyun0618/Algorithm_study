WITH review_avg AS (
    SELECT 
        rest_id,
        ROUND(AVG(review_score), 2) AS score
    FROM rest_review
    GROUP BY rest_id
)

SELECT I.rest_id, I.rest_name, I.food_type, I.favorites, I.address, R.score
FROM rest_info I
    JOIN review_avg R ON I.rest_id = R.rest_id
WHERE address LIKE '서울%'
ORDER BY R.score DESC, I.favorites DESC
