Django Project

Prerequisites:

Ensure you have the following installed on your local machine:

- Python (3.8 or later)
- MySQL Server (5.7 or later)
- pip (Python package installer)

Setup and Installation:

1. Download the project zip file and unzip it to your preferred location.

2. Navigate to the project directory with 'cd djangoProject'.

3. (Optional) Set up a virtual environment:

A virtual environment is to help keep dependencies required by different projects separate by creating isolated Python environments for them.

Below are the commands I used to set up a virtual environment:

a. Install the virtualenv package, which is used to create virtual environments

	 ```pip install virtualenv```
 
	This command installs the `virtualenv` package globally on your system. If this command is executed successfully, you 	should have `virtualenv` available in your system.
 
b. Once virtualenv is installed, navigate to the project directory 'djangoProject' and run the following command to create a new virtual environment:

	 ```virtualenv venv```
 
	The `venv` part is the name of your virtual environment. You can name this anything you like, but `venv` is what I used. 	This command creates a new directory named `venv` (or whatever you named your virtual environment), which contains the 	Python executable files and a copy of the `pip` library which you can use to install other packages in this environment.

c. Activate the virtual environment:
	- On Windows, you can activate the virtual environment using the following command:

     	```source venv\Scripts\activate```
     
 	- On Unix or MacOS, use:

     	```source venv/bin/activate```
     
When the virtual environment is activated, the name of the environment will appear on left side of the terminal which indicates that the environment is currently active. In the terminal, it will look something like this: `(venv) C:\Users\User\djangoproject>`.

While the virtual environment is active, any package that you install using `pip` will be installed in this environment specifically, rather than being installed globally. 

If you start a new terminal session, you will need to reactivate your virtual environment by navigating to your project directory and running the activation command again.

To deactivate the virtual environment and use your normal Python environment, simply type deactivate in the terminal.

4. Install the dependencies i've listed with 'pip install -r requirements.txt'.

5. Set up the database: 
   Open MySQL and create a new database. Then, update the 'DATABASES' configuration in 'djangoProject/settings.py' with your database name, user, password, and other details.

6. Run migrations with 'python manage.py makemigrations' and 'python manage.py migrate'.

7. Create a superuser (for accessing the admin site) with 'python manage.py createsuperuser'.

8. Run the server with 'python manage.py runserver'. You should now be able to access the application at http://localhost:8000.

Usage:

- Access the login page at http://localhost:8000/login
- After login, you will be redirected to the home page at http://localhost:8000/home
- From the home page, click on any inspection entry to see its details at http://localhost:8000/redirect/<id>
- The admin site can be accessed at http://localhost:8000/admin