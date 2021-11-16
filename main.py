from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


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


if __name__ == '__main__':
    # display_scraped_table()
    get_scraped_table()
