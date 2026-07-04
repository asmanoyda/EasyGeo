
# EasyGeo

EasyGeo is an interactive e-learning platform designed to make geography learning simple, engaging, and accessible for students of all levels. The platform offers comprehensive courses covering the geography of different countries, including the United States, India, Japan, and other regions around the world.

*. The course structure is organized in a hierarchical manner to provide a smooth learning experience:

1. Courses – Dedicated to the geography of specific countries or regions.
2. Sections – Each course is divided into multiple sections covering important geographical topics.
3. Units – Every section contains detailed learning units focused on specific concepts.

==> Learning Materials – Each unit includes:
Informative descriptions and explanations
Educational videos for visual learning
Interactive quizzes to assess understanding and reinforce knowledge

* Project Mission:
"Making geography learning easy, interactive, and enjoyable for learners worldwide."

# setting up project
## create venv for isolated environment
``` 
    python3 -m venv myenv
```

```
source ./myenv/bin/activate    
```
## installing requirements
```
pip install -r requirements.txt 
pip list
```

## Create the database
```
python manage.py migrate
```
## load data into database
```

python manage.py loaddata courses/seeders.json
python manage.py loaddata mypage/seeders.json
python manage.py loaddata users/seeders.json


```
## Finally, run the development server:


```
python manage.py runserver

```
python manage.py makemigrations

python manage.py startapp appname



# to do
python manage.py dumpdata courses > seeders.json
python manage.py dumpdata mypage > seeders.json

branch learning

search functions

document for local setup

quiz page fix

profile page

progress bar


update profile html page
#d6f0f5
#deece3