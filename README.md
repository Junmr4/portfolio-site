# portfolio-site

OVERVIEW: This is a portfolio/blog project that i created using django.  


In order to view this project locally on your computer, you must:
1st - clone the project on to your computer.
2nd - pip install -r requirements.txt

Create two files in #portfolio/settings/
- database.py
- secrets.json

The project use posgresql as the database so you will need to create and provided your username and password.
In database.py replace the placeholder with your value,put:


DATABASES = {
		'default':{
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "name of your database",
        "USER":" your username ",
        "PASSWORD":" your password",
        "HOST":"localhost",
        "PORT":"your port number"
   }
}


in secrets.json, put:
{	
	
	"FILENAME":"secrets.json",	
	"SECRET_KEY":" your secret key"	
}

the following line will run the project locally on your computer,

run python manage.py runserver

