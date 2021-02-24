"""
This module contains functions to work with .json file
"""
from pprint import pprint
import json
import requests

def user_input():
    """
    gets information from user

    """
    token = input("Enter a bearer token:")
    name  = input("Enter a screen_name:")
    count = int(input("ENter a count:"))
    return token,name,count


def get_json(bearer_token,screen_name,friends_count):
    """
    gets json file of list of friends using twitter API
    """
    surl = "https://api.twitter.com/1.1/friends/list.json"
    sheaders = {} 
    sheaders["Authorization"] = "Bearer " + bearer_token
    sparams = { 'screen_name': screen_name, 'count': friends_count} 
    response = requests.get(surl, headers=sheaders, params=sparams)
    response_json = response.json()
    with open('data.json', 'w', encoding='utf-8') as file_to_write:
        json.dump(response_json, file_to_write, ensure_ascii=False, indent=4)  
    return response_json


def get_keys_or_list(data):
    """
    Recursive function to go through .json file
    """
    if isinstance(data,list):
        num = int(input("Enter the number of element  of list:\n"))
        new_data = data[num-1]
        indo = get_keys_or_list(new_data)
        return (indo)
    elif isinstance(data,dict):
        keys = []
        for key in data:
            keys.append(key)
        print(keys)
        key = input("Enter a key:\n")
        new_data = data[key]
        indo = get_keys_or_list(new_data)
        return indo
    else:
        return (data)

        



def main():
    """
    main function. Runs the program
    """
    data_tup = user_input()
    data_dict = get_json(data_tup[0],data_tup[1],data_tup[2])
    print(get_keys_or_list(data_dict))

if __name__=="__main__":
    main()