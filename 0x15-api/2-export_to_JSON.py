#!/usr/bin/python3
'''This script gathers data about employees from an api'''
import json
import requests
import sys


if __name__ == "__main__":
    ''' this script is not executd when imported'''
    userId = int(sys.argv[1])
    todoURL = "https://jsonplaceholder.typicode.com/todos"
    usersURL = "https://jsonplaceholder.typicode.com/users/" + sys.argv[1]
    user = requests.get(usersURL)
    if user.status_code == 200:
        user = user.json()
        username = user.get("username")
        todo = requests.get(todoURL)
        todo_json = todo.json()
    userdict = {}
    userlist = []
    for item in todo_json:
        if item.get("userId") == userId:
            userlist.append(item)
    lst = []
    for item in userlist:
        lst.append({item["title"], item["completed"], user["username"]})
    print(lst)
