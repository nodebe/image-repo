# Image Repo Challenge Task

This is a flask application in fulfillment of the shopify backend image repo test. In this app, I have used Flask as the python framework and sqlite as the db for storing data.

## Installation
First off, you have to create and activate a virtual environment to run the application

```bash
virtualenv venv
venv\scripts\activate
```

Then you will have to install the modules required to run this application from the requirements.txt

```bash
pip install -r requirements.txt
```

## Usage

This is a simple application that requires authentication to add images to repo. You can register with any email and password as long as it does not already exist in the database. If it does exist, it redirects to the dashboard of the user. For test purposes you can use the details below:

```
email: tester@gmail.com
password: qwerty1
```
