import csv
import re

import chardet

def write_to_csv(file, data):
    with open(file, 'w') as f_n:
        f_n_writer = csv.writer(f_n)
        for nrow in data:
            f_n_writer.writerow(nrow)


def get_data(lst):
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]

    for i in range(1,4):
        with open(f'info_{i}.txt', 'rb') as file_obj:
            data_bytes = file_obj.read()
            result = chardet.detect(data_bytes)
            data = data_bytes.decode(result['encodind'])

        os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
        os_prod_list.append(os_prod_reg.findall(data)[0].split()[2])

        os_name_reg = re.compile(r'Windows\s*\S*')
        os_name_list.append(os_name_reg.findall(data)[0])


        os_code_reg = re.compile(r'Код продукта:\s*\S*')
        os_code_list.append(os_code_reg.findall(data)[0].split()[2])


        os_type_reg = re.compile(r'Тип системы:\s*\S*')
        os_type_list.append(os_type_reg.findall(data)[0].split()[2])

    data_for_rows = [os_prod_list, os_name_list, os_code_list, os_type_list]

    for idx in range(len(data_for_rows[0])):
        main_data.append([os_prod_list[idx], os_name_list[idx], os_code_list[idx], os_type_list[idx]])
    return main_data



def write_to_csv(out_file):

    main_data = get_data()
    with open(out_file, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in main_data:
            writer.writerow(row)

write_to_csv('data_report.csv')