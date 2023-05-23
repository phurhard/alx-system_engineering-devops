#!/usr/bin/python3
'''This script gathers data about employees from an api'''
import json
import requests
import sys


if __name__ == "__main__":
    ''' this script is not executd when imported'''
    todoURL = "https://jsonplaceholder.typicode.com/todos"
    usersURL = "https://jsonplaceholder.typicode.com/users"
    user = requests.get(usersURL)
    if user.status_code == 200:
        users = user.json()
        todo = requests.get(todoURL)
        todo_json = todo.json()
        user_dict={}
        for user in users:
            username = user.get("username")
            user_id = user.get("id")
            lst = []
            for todos in todo_json:
                if todos.get("userId") == user_id:
                    lst.append({
                        "username": username,
                        "task": todos.get("title"),
                        "completed": todos.get("completed")
                        })
            print(f'{user_id}: {lst}')
            user_dict[f'{user_id}'] = lst


        file = "todo_all_employees.json"
        with open(file, 'w') as wr:
            wr.write(json.dumps(user_dict))
    '''userdict = {}
    userlist = []
    lst = []
    for item in todo_json:
        if item.get("userId") == userId:
            userlist.append(item)
    for item in userlist:
        lst.append({
            "task": item["title"],
            "completed": item["completed"],
            "username": username
            })
    # print(lst)
    userdict[f'{userId}'] = lst
    # print(userdict)
    file = f'{userId}' + '.json'
    with open(file, 'w') as wr:
        wr.write(json.dumps(userdict))'''

