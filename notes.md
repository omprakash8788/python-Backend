### Django API 

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
 






