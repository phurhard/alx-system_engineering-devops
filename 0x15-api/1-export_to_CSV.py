#!/usr/bin/python3
'''This script gathers data about eployees from an api'''

import csv
import json
import sys
import urllib.request as url


if __name__ == "__main__":
    ''' this script is not executd when imported'''
    userId = int(sys.argv[1])
    userTodo = []
    csvData = []
    userName = ""
    with url.urlopen("https://jsonplaceholder.typicode.com/users") as res:
        users = res.read()
        users.decode('utf-8')
        users = json.loads(users)
        for user in users:
            if (user.get('id') == userId):
                userName = user.get('username')
    with url.urlopen("https://jsonplaceholder.typicode.com/todos") as req:
        contents = req.read()
        contents.decode('utf-8')
        contents = json.loads(contents)
        # contents is a list having all todos
        # so we'll loop thrpugh the list
        userTodo.extend(item for item in contents if (item.get('userId') == userId))
        csvData.extend(
            [
                task.get("userId"),
                userName,
                str(task.get("completed")),
                task.get('title'),
            ]
            for task in userTodo
        )
        csv_filename = f"{userId}.csv"
        with open(csv_filename, 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL, delimiter=',')
            writer.writerows(csvData)
