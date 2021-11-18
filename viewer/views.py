from django.shortcuts import render
from django.db import connection


def display_data(request):
    cursor = connection.cursor()
    cursor.execute('''
        SELECT order_date, region.name, rep.name, item.name, quantity, total_discount, final_price
        FROM orders
        INNER JOIN item on orders.item_id = item.id
        INNER JOIN rep on orders.rep_id = rep.id
        INNER JOIN region on rep.region_id = region.id
        INNER JOIN payment on orders.id = payment.order_id;
        ''')
    data = cursor.fetchall()
    return render(request, 'index.html', {'data': data})
