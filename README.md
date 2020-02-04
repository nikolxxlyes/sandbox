# Lodal payment 
Django project payment on sandbox.coingate.com
(include sqlite)

Install venv with  >>> requirements.txt

Instruction for run site >>> 

1. Deploy the application to the server.
    (For example in: Linux, Heroku, Ngrok)

2. Enter new received web address to 
/Sandbox/project/setting.py['ALLOWED_HOSTS]
instead '3a850329.ngrok.io'

3. Sing in https://sandbox.coingate.com/
    
        email: giwaj21438@reptech.org
        password: UqasAEZkWEKH6rG
    
4. In page https://sandbox.coingate.com/account/business/manage#settings
   option 'Website address' add a new address(p.2 this instruction).
   Delete old website, like 'http://3a850329.ngrok.io'.

5. Run your project.(Where you push this application) and smile :)
    
For example, you can use Ngrok application. Install it and set the command: 
"ngrok http 127.0.0.1:8000" ).

After that in Pycharm command: "python manage.py runserver" 

All rights reserved # Lodal Group Industry