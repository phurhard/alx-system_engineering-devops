#!/usr/bin/python3
'''This script gathers data about eployees from an api'''
import json
import urllib.request as url
import sys


if __name__ == "__main__":
    ''' this script is not executd when imported'''
    userId = sys.argv[1]
    userId = int(userId)
    userTodo = []
    userName = ""
    with url.urlopen("https://jsonplaceholder.typicode.com/users") as res:
        users = res.read()
        users.decode('utf-8')
        users = json.loads(users)
        for user in users:
            if (user.get('id') == userId):
                userName = user.get('name')
    with url.urlopen("https://jsonplaceholder.typicode.com/todos") as req:
        contents = req.read()
        contents.decode('utf-8')
        contents = json.loads(contents)
        # contents is a list having all todos
        # so we'll loop thrpugh the list
        for item in contents:
            if (item.get('userId') == userId):
                userTodo.append(item)
        TNOT = len(userTodo)
        NODT = 0
        for task in userTodo:
            if (task.get('completed') is True):
                NODT = NODT + 1
        print(f"Employee {userName} is done with tasks({NODT}/{TNOT}):")
        for item in userTodo:
            if (item.get('completed') is True):
                print(f"\t {item.get('title')}")
