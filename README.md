### Project for health++ backend

In order to setup project depedencies you'll need virtualenv
```sh
$ pip3 install virtualenv
$ virtualenv -p python3 env
$ source env/bin/activate
```

Project setup
```sh 
$ pip install -r requirements.txt
$ gunicorn --bind 0.0.0.0:8000 wsgi
```