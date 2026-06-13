pip install django
pip uninstall django
pip list
source ./venv/bin/activate    

python manage.py runserver
python manage.py makemigrations
python manage.py migrate

python manage.py dumpdata mysite > seeders.json

python manage.py loaddata mysite > seeders.json





## to do

decouple application code (appps)

search functions

document for local setup

profile dropdown

progress bar

requirement.txt

fixtures django
