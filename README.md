# Grade App
![I failed](./myapp/static/myapp/failure.png)
Grade App is web application. It is written in python, html, css, javascript. Third party tools include 
[Django](https://docs.djangoproject.com/), MySQL, [D3](https://d3js.org/),[plot.js](https://observablehq.com/plot/getting-started). It allows instructors to fill in, amend and visualize grades of their students.

# How to Use It
After cloning the repository, run:
```sh
python manage.py runserver
```
to start the app. Note that you must have `MySQL` installed on your host machine and have created an database named `grade`.

To create admins, run:
```sh
python manage.py createsuperuser
```
and follow its instructions.

# Deploy Using Docker
To deploy using docker, run:
```sh
docker-compose up --build
```
and then `manually` run 
```sh
python manage.py makemigrations
python manage.py migrate 
```
in the terminal of the container.

# Further Reading
For more information about this app, read the docs of it in `users/templates/help.html`.