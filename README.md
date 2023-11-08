# Backend for Software Engineering Project
This is the backend code written in Django for the ABC Management Inc. client management system. It will act as the mediator between the frontend and database of the project.
## How to get this repo working on your local machine
> **_NOTE:_** You must first start your MySQL Server on your local machine. (Make sure it can be connected to through MySQLWorkbench)
1. Clone this repo onto your local machine.
2. Navigate to the `software-engineering-project-backend/swe-project-backend-api` folder. (You will know if you are in the right folder if you see the requirements.txt file)
3. Run the following command in your terminal from the directory:
   > pip install -r requirments.txt
5. Navigate to the `software-engineering-project-backend/swe-project-backend-api/sweClassProjectBackend/sweClassProjectBackend` folder. (You will know if you are in the right folder if you see the settings.py file)
6. Create a file named `".env"`. (Ensure that the file extension of this file is .env and not anything else)
7. In this file create **3** variables using this format:
    > SQL_PASSWORD={`Your Password to your mySQL instance`}
    > 
    > > Ex: SQL_PASSWORD=***specialpassword***
    > 
    > SQL_USERNAME={`Your username to your mySQL instance`}
    > 
    > > Ex: SQL_USERNAME=***specialusername***
    > 
    > SECRET_KEY={**CONTACT ME FOR THE KEY** ***via text or email***}
8. Now navigate to the `software-engineering-project/swe-project-backend-api/sweClassProjectBackend` folder (You will know if you are in the right folder if you see the manage.py file) and run the following command:
    > python3 manage.py runserver
9. You may have to migrate the changes from the Django project to your mySQL instance but the command line will tell you the commands to do so.
