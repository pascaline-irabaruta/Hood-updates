<p>
<a href="https://hoodpascy.herokuapp.com/" target="_blank">
  <h1 align="center" style="color:black;">Hood-Updates ...</h1>
</a>
</p>
An web application that allows users to join neighbourhood and loop through everything that happens in the neighbourhood.

### Technologies used

1. Python3
2. SQLite3
3. Bootstrap 4.8.10
4. jQuery 3.4.1
5. Django 1.11.23
6. Html & Css

### Requirements

This project requires python3 to run

### Setting up a virtual environement

To create a virtual environement, you will need to install virtualenv
```sh
pip3 install virtualenv
```

Create the virtual environement by running the command in the project root
```sh
virtualenv venv
```

Activate the virtual environement by running the command
```sh
source venv/bin/activate
```

You can always deactivate the virtual environement by entering this command
```sh
deactivate
```

### Usage

Make migrations by using the command
```sh
python manage.py migrate
```

You need to create a .env file and set your secret key inside it. To launch the app, simply run the command
```sh
 python manage.py runserver
```

### Run tests

```sh
python manage.py test
```

### Author

👤 **Pascaline Irabaruta**

* Github: [@pascyirabaruta](https://github.com/pascaline-irbaruta)
* Email:pascyirabaruta456@gmail.com


#### This project is licensed under MIT [LICENSE.md](LICENSE.md) 
