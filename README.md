Features

Create Account and login(3 Users :- # Photographer ## Guide ### Traveller)
Edit Profile (first name, last name, bio, charges ,etc)
Add photo
Forgot passowrd
Add Description
Filter by Charges,Place,Review
Order
Mail Order
Review
My Order
Forget password - NOTE == when you enter your email id make sure you have entered correct email id because in wrong email id it will not send you the unique link, you will see that link in your Email

Project requirement

you can install packages one by one from here
pip install django
pip install pillow
Pip install mysqlcilent


Steps
Step 1 - Run Xampp.

Step 2 - start my sql server click on Admin and create a new table SMT.
 
Step 3 - go in directory where manage.py file is present and run command given bellow
python manage.py makemigrations

Step 4 - if you want you can create super user to see the admin panel by bellow command
python manage.py createsuperuser

Step 5 - run command given bellow
python manage.py migrate

Step 6 - After above step you can directly run project by bellow command
python manage.py runserver
