#Holberton School - AirBnB_clone
This project is a clone of the website AirBnB.

## Usage:
Interactive Mode:
How to ask for help:
```
PROMPT~> ./console.py
(hbtn) help

Documented Commands (type help <topic>)
======================================
EOF   help   quit

(hbtn)
(hbtn)
(hbtn) quit
PROMPT~>
```
How to list all instances of a class:
```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.all()
[[User] (ec6c5aa4-ebd3-11e6-864c-08002745538c) {'id': 'ec6c5aa4-ebd3-11e6-864c-08002745538c', 'email': 'airbnb@holbertonshool.com', '__class__': 'User', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 1, 15, 18, 50, 11, 853163), 'first_name': 'Betty', 'updated_at': datetime.datetime(2017, 1, 15, 18, 50, 11, 853222), 'password': 'root'}, [User] (edaab9ce-ebd3-11e6-a4af-08002745538c) {'id': 'edaab9ce-ebd3-11e6-a4af-08002745538c', 'email': 'airbnb@holbertonshool.com', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 1, 15, 18, 50, 13, 939549), 'first_name': 'Betty', 'password': 'root', 'updated_at': datetime.datetime(2017, 1, 15, 18, 50, 13, 939585)}]
(hbnb)
```
How to count instances of a class:
```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.count()
2
(hbnb)
```
How to show an instance from a ID:
```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.show("ec6c5aa4-ebd3-11e6-864c-08002745538c")
[User] (ec6c5aa4-ebd3-11e6-864c-08002745538c) {'id': 'ec6c5aa4-ebd3-11e6-864c-08002745538c', 'email': 'airbnb@holbertonshool.com', '__class__': 'User', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 1, 15, 18, 50, 11, 853163), 'first_name': 'Betty', 'updated_at': datetime.datetime(2017, 1, 15, 18, 50, 11, 853222), 'password': 'root'}
(hbnb) User.show("Holberton")
** no instance found **
(hbnb)
```
How to destroy an instance:
```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.count()
2
(hbnb) User.destroy("ec6c5aa4-ebd3-11e6-864c-08002745538c")
(hbnb) User.count()
1
(hbnb) User.destroy("Holberton")
** no instance found **
(hbnb)
```
How to update an instance:
```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.show("ec6c5aa4-ebd3-11e6-864c-08002745538c")
[User] (ec6c5aa4-ebd3-11e6-864c-08002745538c) {'id': 'ec6c5aa4-ebd3-11e6-864c-08002745538c', 'email': 'airbnb@holbertonshool.com', '__class__': 'User', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 1, 15, 18, 50, 11, 853163), 'first_name': 'Betty', 'updated_at': datetime.datetime(2017, 1, 15, 18, 50, 11, 853222), 'password': 'root'}
(hbnb) User.update("ec6c5aa4-ebd3-11e6-864c-08002745538c", "first_name", "John")
(hbnb) User.update("ec6c5aa4-ebd3-11e6-864c-08002745538c", "age", 89)
(hbnb) User.show("ec6c5aa4-ebd3-11e6-864c-08002745538c")
[User] (ec6c5aa4-ebd3-11e6-864c-08002745538c) {'id': 'ec6c5aa4-ebd3-11e6-864c-08002745538c', 'email': 'airbnb@holbertonshool.com', '__class__': 'User', 'last_name': 'Holberton', 'created_at': datetime.datetime(2017, 1, 15, 18, 50, 11, 853163), 'first_name': 'John', 'updated_at': datetime.datetime(2017, 1, 15, 18, 50, 11, 853222), 'password': 'root', 'age': 89}
(hbnb)
```

Non-Interactive Mode:
```
PROMPT~> echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
PROMPT~> cat test_help
help
PROMPT~> cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
PROMPT~>
```

## Authors:
Jennie Chu & Sam Scislowicz