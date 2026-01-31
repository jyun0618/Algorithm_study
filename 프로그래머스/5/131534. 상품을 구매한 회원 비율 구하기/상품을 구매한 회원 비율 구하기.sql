WITH joined_2021 AS ( -- 2021년 가입 회원 목록
  SELECT 
    user_id
  FROM user_info
  WHERE joined >= '2021-01-01' AND JOINED < '2022-01-01'
),

total_2021 AS ( -- 2021년 가입 회원 수
  SELECT 
    COUNT(user_id) AS total_cnt
  FROM joined_2021
),

monthly_user AS ( -- 2021년 가입 회원 중 월별 구매 회원 목록
  SELECT
    YEAR(os.sales_date)  AS year,
    MONTH(os.sales_date) AS month,
    os.user_id
  FROM online_sale AS os
  JOIN joined_2021 AS j
    ON os.user_id = j.user_id
  GROUP BY year, month, os.user_id
)

SELECT
    year,
    month,
    COUNT(user_id) AS purchased_users,
    ROUND(
        COUNT(user_id) / (
            SELECT COUNT(user_id) FROM joined_2021
        ),
        1
    ) AS puchased_ratio
FROM monthly_user
GROUP BY year, month
ORDER BY year, month