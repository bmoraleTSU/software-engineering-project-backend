# Backend for Software Engineering Project
This is the backend code written in Django for the ABC Management Inc. client management system. It will act as the mediator between the frontend and database of the project.
## How to get this repo working on your local machine
1. Clone this repo onto your local machine.
2. Navigate to the `software-engineering-project-backend/swe-project-backend-api/sweClassProjectBackend/sweClassProjectBackend` folder. (You will know if you are in the right folder if you see the settings.py file)
3. Create a file named `"mySQLVariables.env"`. See [this](https://www.oreilly.com/library/view/javascript-by-example/9781788293969/d34ba441-abb3-4937-acf1-a2e7d54ffb23.xhtml) link for help creating a **.env** file on Windows. (ensure that the file extension of this file is .env and not anything else)
4. In this file create **3** variables using this format:
    > SQL_PASSWORD={`Your Password to your mySQL instance`}
    >
    > SQL_USERNAME={`Your username to your mySQL instance`}
    >
    > SECRET_KEY={**CONTACT ME FOR THE KEY** ***via text or email***}
5. Now navigate to the `software-engineering-project/swe-project-backend-api/sweClassProjectBackend` folder and run the following command:
    > python3 manage.py runserver
6. You may have to migrate the changes from the Django project to your mySQL instance but the command line will tell you the commands to do so.