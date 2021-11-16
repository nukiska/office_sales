import pymysql as pymysql
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from create_queries import execute_create_queries
from insert_queries import execute_insert_queries


def display_scraped_table():
    """Procedure displays scraped HTML table as DataFrame object using Pandas"""
    import pandas as pd
    import requests
    r = requests.get('https://www.contextures.com/xlsampledata01.html')
    r.status_code
    tables = pd.read_html(r.text)
    print(tables[0])


def get_scraped_table() -> list:
    """
    Function scrapes HTML table using Selenium and returns the list of tuples
    where each tuple represents one table row excluding the first one
    """

    path = r'C:\Users\ninag\selenium\chromedriver.exe'
    service_obj = Service(path)

    try:
        with webdriver.Chrome(service=service_obj) as driver:
            driver.get('https://www.contextures.com/xlsampledata01.html')
            table = driver.find_element(By.TAG_NAME, 'tbody')
            rows = table.find_elements(By.TAG_NAME, 'tr')

            rows_list = []
            for r in range(1, len(rows)):
                rows_list.append(tuple(rows[r].text.split('\n')))
        return rows_list

    except Exception:
        return []

    finally:
        for row in rows_list:
            print(row)


def main() -> list:
    """
    Function connects to the database, creates a new schema with new tables.
    Then, it recalculates the scraped table according to the specified conditions
    and returns the new table as a list of tuples.
    """

    db = pymysql.connect(host='localhost', user='nina', password='ninaheslo', database='')
    try:
        execute_create_queries(db)
        with db.cursor() as c:
            c.execute('''USE `office_sales_db`;''')

            new_rows_list = []

            for row_tuple in get_scraped_table():
                for i in range(len(row_tuple)):
                    if i == 0:
                        date = row_tuple[i].split('/')
                        order_date = '-'.join([date[2], date[0], date[1]])
                    elif i == 1:
                        region = row_tuple[i]
                    elif i == 2:
                        rep = row_tuple[i]
                    elif i == 3:
                        item = row_tuple[i]
                    elif i == 4:
                        units = int(row_tuple[i])
                    elif i == 5:
                        unit_cost = float(row_tuple[i])
                    elif i == 6:
                        if ',' in row_tuple[i]:
                            string_elem = row_tuple[i]
                            string_elem = string_elem.replace(',', '')
                            total_price = float(string_elem)
                        else:
                            total_price = float(row_tuple[i])

                if region == 'Central':
                    unit_discount = 0.23
                else:
                    unit_discount = 0.12

                if region == 'East' and units > 50:
                    extra_discount = 7.2
                else:
                    extra_discount = 0

                total_discount = unit_discount * units + extra_discount
                final_price = total_price - total_discount

                new_row_tuple = (order_date, region, rep, item, units, total_discount, final_price)
                new_rows_list.append(new_row_tuple)

                execute_insert_queries(db, region, item, rep, units, order_date, final_price, total_discount)

    finally:
        db.close()

        for new_row in new_rows_list:
            print(new_row)

        return new_rows_list


if __name__ == '__main__':
    # display_scraped_table()
    # get_scraped_table()
    main()
