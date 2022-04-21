import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', encoding='utf-8') as f_n:
        dict_to_json = json.load(f_n)
        print(dict_to_json)
        dict_to_json['orders'].append({
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date,
        })
    with open ('orders.json',  'w', encoding='utf-8', ) as f_n:
        json.dump(dict_to_json, f_n, indent=4, ensure_ascii=False)



write_order_to_json('Стул', 1, 100, 'Ivan', '01.01.2022')
write_order_to_json('table', 2, 200, 'Petr', '02.02.2022')
write_order_to_json('pen', 3, 300, 'Сергей', '03.03.2022')
write_order_to_json('pencil', 4, 400, 'Yan', '04.04.2022')



