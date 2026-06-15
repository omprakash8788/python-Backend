### Django API 
## CP/01/26

*** Setup ***
''' Check current python version 
 - python --version
'''

`Create new directory`
 > mkdir code
 > cd code

`To exit `
 > exit 

`Confirm python version`
 > python --version

## Virtual Environments 
 - Create in the root of folder 
 > python -m venv .venv

 `After that active virtual environment`
 > .venv\Scripts\Activate.ps1

*** To deactivate and leave a virtual environment type deactivate. ***
 > (.venv) PS D:\python-backend> deactivate

*** Install Django and Django REST Framework ***
 `pip install Django`
 `python -m pip install "djangorestframework~=3.13.0"`

## The commandpip freeze outputs the contents of your current virtual environment.
 ***
 (.venv) PS D:\python-backend> pip freeze
  asgiref==3.11.1
  Django==6.0.6
  djangorestframework==3.13.1
  pytz==2026.2
  sqlparse==0.5.5
  tzdata==2026.2
  (.venv) PS D:\python-backend> 
 ***

- It is a standard practice to output the contents of a virtual environment to a file called
 requirements.txt.This is a way to keep track of installed packaged and also let so the developers
 recreate the virtual environment on different computers. Let’s do that now by using the >
 operator.

`(.venv) PS D:\python-backend> pip freeze > requirements.tsx `
 - If you look in the setup directory there is now an additional file called requirements.txt. 


*** Text Editors   ***
 - Upto you, in my case i am using vs code


### CP-02/26
*** Web APIs ***
`REST- Representatinal state transfer`

### CP-03/26


### Traditional Django
- Navigate to the existing code directory on the Desktop and make sure you are not in a current
  virtual environment. You should not see (.venv) before the shell prompt. If you do, use the
  command deactivate to leave it. Make a new directory called library, create a new virtual
  environment, activate it, and install Django.

(.venv) PS D:\python-backend> deactivate `# 1`
PS D:\python-backend> cd code `# 2`
PS D:\python-backend\code> mkdir library `# 3`


    Directory: D:\python-backend\code


Mode                 LastWriteTime         Length Name                                                                                         
----                 -------------         ------ ----                                                                                         
d-----         6/13/2026  12:19 PM                library                                                                                      


PS D:\python-backend\code> cd library `# 4`
PS D:\python-backend\code\library> python -m venv .venv `# 5`
PS D:\python-backend\code\library> .venv\Scripts\Activate.ps1 `# 6`
(.venv) PS D:\python-backend\code\library> `Now our env is activated`

Atraditional Django website consists of a single project with multiple apps representing discrete
functionality. Let’s create a new project with the start project command called django_project.
Don’t forget to include the period . at the end which installs the code in our current directory.
If you do not include the period, Django will create an additional directory by default.

## install 

- pip install django 

## Then create the project 
- $ python -m django startproject django_project .
(.venv) 

├── django_project
│ ├── __init__.py
| ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── manage.py
└── .venv/

The manage.py file is not part of django_project but is used to execute various Django com
mandssuchasrunning the local web server or creating a new app. Let’s use it now with migrate
to sync thedatabase with Django’s default settings and start up the local Django web server with
runserver.

ompra@OMPRAk-DE-ASUS-PR MINGW32 /d/python-backend/code/library (main)
$ python manage.py migrate

- After migrate run server

ompra@OMPRAk-DE-ASUS-PR MINGW32 /d/python-backend/code/library (main)
$ python manage.py runserver


- After that - open it, http://127.0.0.1:8000/



### First app

The next step is to add our first app which we’ll call books. Stop the local server by typing
Control+c and then run the startapp command plus our app name to create it.

` python manage.py startapp books`

- Nowlet’s explore the app files Django has automatically created for us.

├── books
│ ├── __init__.py
│ ├── admin.py
│ ├── apps.py
│ ├── migrations
│ │ └── __init__.py
│ ├── models.py
│ ├── tests.py
│ └── views.py


Each app has a __init__.py file identifying it as a Python package and there are 6 new files
created:
• admin.py is a configuration file for the built-in Django Admin app
• apps.py is a configuration file for the app itself
• migrations/ is a directory that stores migrations files for database changes
• models.py is where we define our database models
• tests.py is for our app-specific tests
• views.py is where we handle the request/response logic for our web app


# admin 
user name -op
email - op@gmail.com
pw- AS##8788364473

## Ch-04/26  Library API


## Ch-05/26 Todo API

## Ch-06/26 Blog API




