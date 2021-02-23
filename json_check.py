from pprint import pprint
import json

def read_and_convert(path):
    """
    reads and converts json file to python objects
    """
    with open(path, 'r', encoding='UTF-8') as file_tto_read:
        data = json.load(file_tto_read)
        return data

def get_keys_or_list(data):
    if isinstance(data,list):
        num = int(input("enter the number of element"))
        new_data = data[num-1]
        indo = get_keys_or_list(new_data)
        return (indo)
    elif isinstance(data,dict):
        keys = []
        for key in data:
            keys.append(key)
        print(keys)
        key = input("enter a key:\n")
        new_data = data[key]
        indo = get_keys_or_list(new_data)
        return indo
    else:
        return (data)

        



def main():
    data_dict = read_and_convert('kved.json')
    print(get_keys_or_list(data_dict))


main()