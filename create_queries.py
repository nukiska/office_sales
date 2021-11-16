def execute_create_queries(db):
    """Procedure connects to the database, creates a new schema with new tables in it."""

    with db.cursor() as c:
        c.execute('''DROP DATABASE IF EXISTS `office_sales_db`;''')
        c.execute('''CREATE SCHEMA IF NOT EXISTS `office_sales_db` DEFAULT CHARACTER SET `utf8`;''')
        c.execute('''USE `office_sales_db`;''')

        c.execute('''DROP TABLE IF EXISTS `office_sales_db`.`region`;''')

        c.execute('''CREATE TABLE IF NOT EXISTS `office_sales_db`.`region` (
                    `id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
                    `name` VARCHAR(30) NOT NULL,
                    PRIMARY KEY (`id`)
                );''')

        c.execute('''DROP TABLE IF EXISTS `office_sales_db`.`item`;''')

        c.execute('''CREATE TABLE IF NOT EXISTS `office_sales_db`.`item` (
                    `id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
                    `name` VARCHAR(30) NOT NULL,
                    PRIMARY KEY (`id`)
                );''')

        c.execute('''DROP TABLE IF EXISTS `office_sales_db`.`rep`;''')

        c.execute('''CREATE TABLE IF NOT EXISTS `office_sales_db`.`rep` (
                    `id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
                    `name` VARCHAR(30) NOT NULL,
                    `region_id` SMALLINT UNSIGNED NOT NULL,
                    PRIMARY KEY (`id`),
                    FOREIGN KEY (`region_id`) REFERENCES `office_sales_db`.`region`(`id`)
                );''')

        c.execute('''DROP TABLE IF EXISTS `office_sales_db`.`rep_item`;''')

        c.execute('''CREATE TABLE IF NOT EXISTS `office_sales_db`.`rep_item` (
                    `rep_id` SMALLINT UNSIGNED NOT NULL,
                    `item_id` SMALLINT UNSIGNED NOT NULL,
                    FOREIGN KEY (`rep_id`) REFERENCES `office_sales_db`.rep(`id`),
                    FOREIGN KEY (`item_id`) REFERENCES `office_sales_db`.item(`id`),
                    PRIMARY KEY (`rep_id`,`item_id`)
                );''')

        c.execute('''DROP TABLE IF EXISTS `office_sales_db`.`orders`;''')

        c.execute('''CREATE TABLE IF NOT EXISTS `office_sales_db`.`orders` (
                    `id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
                    `item_id` SMALLINT UNSIGNED NOT NULL,
                    `quantity` INTEGER NOT NULL CHECK (`quantity` >= 0),
                    `rep_id` SMALLINT UNSIGNED NOT NULL,
                    `order_date` DATE NOT NULL,
                    PRIMARY KEY (`id`),
                    UNIQUE INDEX `id_UNIQUE` (`id` ASC),
                    FOREIGN KEY (`item_id`) REFERENCES `office_sales_db`.item(`id`),
                    FOREIGN KEY (`rep_id`) REFERENCES `office_sales_db`.rep(`id`)
                );''')

        c.execute('''DROP TABLE IF EXISTS `office_sales_db`.`payment`;''')

        c.execute('''CREATE TABLE IF NOT EXISTS `office_sales_db`.`payment` (
                    `id` SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
                    `order_id` SMALLINT UNSIGNED NOT NULL,
                    `final_price` DECIMAL(10,2) NOT NULL CHECK (`final_price` >= 0),
                    `total_discount` DECIMAL(10,2) NOT NULL CHECK (`total_discount` >= 0),
                    `creation_date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                     PRIMARY KEY (`id`),
                     UNIQUE INDEX `id_UNIQUE` (`id` ASC),
                     FOREIGN KEY (`order_id`) REFERENCES `office_sales_db`.orders(`id`) ON DELETE CASCADE
                );''')
        db.commit()
