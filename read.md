### create virtaul env
python - m venv venv
### activate venv
. venv/bin/activate
### install django packages
pip install django djangorestframework
### create a prject
   __add . in the end for creating project in same directory__
django-admin startproject PROJ_NAME .
### run the project
python manage.py runserver
### create an application
python manage.py startapp APP_NAME
### create models for the app
python manage.py makemigrations
### migrate the data into database
python manage.py migrate
### create admin user
python manage.py createsuperuser
### add model to admin.py
admin.site.register(MODEL_NAME)

-- add app to settings.py
-- add serializer.py
-- update view.py
-- add urls.py
-- map to global urls