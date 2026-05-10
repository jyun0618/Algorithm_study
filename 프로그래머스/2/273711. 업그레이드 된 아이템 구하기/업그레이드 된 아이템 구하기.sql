# -- 코드를 작성해주세요
# WITH PARENT AS (
# SELECT T.ITEM_ID, T.PARENT_ITEM_ID FROM ITEM_TREE T
#     JOIN (SELECT ITEM_ID, RARITY FROM ITEM_INFO
#             WHERE RARITY = 'RARE') I
#     ON T.PARENT_ITEM_ID = I.ITEM_ID)
    
# SELECT P.ITEM_ID, C.ITEM_NAME, C.RARITY FROM ITEM_INFO C
#     JOIN PARENT P ON C.ITEM_ID = P.ITEM_ID
# WHERE P.PARENT_ITEM_ID IS NOT NULL
# ORDER BY ITEM_ID DESC;



    SELECT
        child.item_id,
        child.item_name,
        child.rarity
    FROM item_info AS parent
        INNER JOIN item_tree AS tree
            ON parent.item_id = tree.parent_item_id
        INNER JOIN item_info AS child
            ON tree.item_id = child.item_id
    WHERE 1=1
        AND parent.rarity = 'RARE' -- 부모 아이템의 희귀도 'RARE'
    ORDER BY child.item_id DESC
