# NDHPbackend

## Create Env
Install the virtual environment `python3 -m pip install --user virtualenv`
Create it `python3 -m venv env`
Activate it `source env/bin/activate`

## Requirements
Install the requirements `pip install -r requirements.txt`

If that does not work, go into the requirements file and pip install all of the requirements

## Change settings
The backend/backend/settings.py file will need to be changed in order to run this locally. You need to change `SECRET_KEY` `DATABASES` `EMAIL_HOST_USER` `EMAIL_HOST_PASSWORD` `SEND_EMAIL_USER`

## Run
`python3 manage.py runserver`

## Useful Commands
`python3 manage.py makemigrations` preps the database for the models
`python3 manage.py migrate` makes the models in the database
