# Office sales

This example was made to demonstrate basic knowledge of web scraping, working with data and the basics of working with a database.

- used Python version 3.9
- MySQL database with PyMySQL package

### 1. Data acquisition

Scrape table **Office Supply Sales Table** from [https://www.contextures.com/xlsampledata01.html](https://www.contextures.com/xlsampledata01.html)

>As output can be used any data type (dict, list, Pandas DataFrame …)

### 2. Calculations

Calculate **final discount** for each record downloaded from step 1 based on conditions below.
- for data with region Central is unit discount 0.23 $
- for each other region is unit discount 0.12 $
- for more than 50 units is calculated **extra discount** 7.2 $
-- this extra discount is only for records from East region

### 3. Output

Prepare output and save data into database.
- Prepare database structure
- Save only:
-- Region, Rep, Item, Units, Total discount, Final price, Creation date, Order date


>Final price is based on step 2, where final price is total price with all calculated discounts.<br />
>Total discount is summary of unit discount and extra discount.<br />
>Creation date is actual DateTime.
