# test_task_for_insert
## Setup
To run this project, install it locally using Docker:

```
$ git clone https://github.com/mrsmugliy/test_task_for_insert
$ cd test_task_for_insert
$ docker-compose up --build
```
OR
```
$ git clone https://github.com/mrsmugliy/test_task_for_insert
$ cd test_task_for_insert\portal_with_advertisements
$ python3 -m venv <name_of_virtualenv>
$ pip install -r requirements.txt
$ python3 manage.py runserver

$ cd test_task_for_insert\angular\angular-app
$ npm start
```
## Ports

the API backend is under the port ```8000```
the frontend is under the port ```8080```



in case of error ```"standard_init_linux.go:219: exec user process caused: no such file or directory"```
in the file "portal_with_advertisements/docker-entrypoint.sh", you need to change from CRLF to LF.
