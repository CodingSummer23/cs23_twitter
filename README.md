# Twitter Clone
## Django exercise for Coding Summer 23

The outcome of each week is in a respective branch (week-x)   
The main branch has the latest update.   

## Instruction to clone and run  
1. Clone the project: ```git clone https://github.com/CodingSummer23/cs23_twitter.git```   
1. Go to the project's folder: ```cd cs23_twitter``` 
1. Create a virtual enviroment: ```python -m venv venv```  
1. Activate venv: (Mac/Linux: ```source venv/bin/activate```) (Win: ```venv\Scripts\activate```)  
1. Install required packages: ```pip install -r requirements.txt``` 
1. Go into the project's folder: ```cd twitter_clone```
1. Migrate database: ```python manage.py migrate``` 
1. Create a superuser: ```python manage.py createsuperuser``` and follow the instractions
1. Start the server: ```python manage.py runserver```

## Week 1
We created the project, added a ``tweets``` application and created the Tweet model. Then created a simple ```feed``` page to check database connectivity.