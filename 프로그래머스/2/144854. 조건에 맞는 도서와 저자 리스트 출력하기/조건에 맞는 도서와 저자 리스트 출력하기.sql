SELECT 
    book_id,
    author_name,
    date_format(published_date, '%Y-%m-%d') AS published_date
FROM book AS b
    JOIN author AS a
        ON b.author_id = a.author_id
WHERE b.category = '경제'
ORDER BY published_date