
import yaml


def data_dict(data):

    with open('file.yaml', 'w', encoding='utf-8') as file:
        yaml.dump(data, file, default_flow_style=False, allow_unicode=True)


def read_dict():
    try:
        with open('file.yaml', 'r', encoding='utf-8') as new_file:
            content = yaml.load(new_file)
            return content
    except FileNotFoundError:
        print('данные не считываются')



new_dict = {1: ['a', 'b', 'c', 'd'],
            2: 12345,
            3: {1: '\u03E0', 2: '\u0480', 3: '\u04A6'}
}

data_dict(new_dict)

print(read_dict())

print(read_dict()==read_dict())


