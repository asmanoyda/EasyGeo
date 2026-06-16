
# EasyGeo

about page

# setting up project
## create venv for isolated environment
``` 
    python3 -m venv myenv
```

```
source ./venv/bin/activate    
```
## installing requirements
```
pip install -r requirements.txt --user
pip list
```

## Create the database
```
python manage.py migrate
```
## load data into database
```

python manage.py loaddata courses/seeders.json
python manage.py loaddata mysite/seeders.json
python manage.py loaddata users/seeders.json


```
## Finally, run the development server:


```
python manage.py runserver

```
python manage.py makemigrations

python manage.py startapp appname



# to do
python manage.py dumpdata mysite > seeders.json

branch learning

search functions

document for local setup

quiz page fix

profile page

progress bar


update profile html page
