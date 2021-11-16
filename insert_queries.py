def execute_insert_queries(db, region, item, rep, units, order_date, final_price, total_discount):
    """Procedure connects to the database and inserts data into tables."""

    with db.cursor() as c:
        c.execute('''USE `office_sales_db`;''')
        c.execute('''INSERT INTO `office_sales_db`.`region`(name)
                    SELECT * FROM (SELECT %s AS name) AS tmp
                    WHERE NOT EXISTS (
                    SELECT name FROM `office_sales_db`.`region` WHERE name = %s
                    ) LIMIT 1;
                ''', (region, region))

        c.execute('''INSERT INTO `office_sales_db`.`item`(name)
                    SELECT * FROM (SELECT %s AS name) AS tmp
                    WHERE NOT EXISTS (
                    SELECT name FROM `office_sales_db`.`item` WHERE name = %s
                    ) LIMIT 1;
                ''', (item, item))

        c.execute('''INSERT INTO `office_sales_db`.`rep`(name, region_id)
                    SELECT * FROM (SELECT %s AS name,
                    (SELECT id FROM `office_sales_db`.`region` WHERE name = %s) AS region_id) AS tmp
                    WHERE NOT EXISTS (
                    SELECT name FROM `office_sales_db`.`rep` WHERE name = %s
                    ) LIMIT 1;
                ''', (rep, region, rep))

        c.execute('''INSERT INTO `office_sales_db`.`orders`(item_id, quantity, rep_id, order_date)
                    VALUES (
                    (SELECT id FROM `office_sales_db`.`item` WHERE name = %s),
                    %s,
                    (SELECT id FROM `office_sales_db`.`rep` WHERE name = %s),
                    %s);
                ''', (item, units, rep, order_date))

        c.execute('''INSERT INTO `office_sales_db`.`payment`(order_id, final_price, total_discount)
                    VALUES (
                    (SELECT id FROM `office_sales_db`.`orders` WHERE order_date = %s),
                    %s, %s);
                ''', (order_date, final_price, total_discount))
        db.commit()
