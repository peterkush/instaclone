# instaclone

#### Author:
peter kungu


## Description
This is an application that allows users to sign up, upload pictures,view other user's pictures,like them, comment on them  follow the other users and delete post.

## Setup and installations

* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3.6 manage.py runserver`
* Access the live site using the local host provided

### Prerequisites
* python3.6 and above
* virtual environment
* pip

##### Clone the Repo 
 https://github.com/peterkush/instaclone

 #### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```
#### Create and activate the virtual environment
```bash
python3.6 -m venv virtual
```

```bash
source virtual/bin/activate
```
#### Setting up environment variables
Create a `.env` file and paste the following. Replace with your own values:


 *DEBUG=True
 *DB_NAME='ig'
*DB_USER='<your database name>'
*DB_PASSWORD='<password to your database>'
*DB_HOST='127.0.0.1'
*MODE='dev'
*ALLOWED_HOSTS='*'
*DISABLE_COLLECTSTATIC=1
```


#### Install dependencies
Install dependencies that will create an environment for the app to run
`pip install -r requirements.txt`


#### Make and run migrations
```bash
python3.6 manage.py check
python manage.py makemigrations instagram
python3.6 manage.py sqlmigrate instagram 0001
python3.6 manage.py migrate
```



#### Run the app
```bash
python3.6 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)



## Technologies 

* [Python3.6](https://docs.python.org/3/)
* Django 3.3.1
* Postgresql 
* Boostrap3
* HTML
* CSS



### License

* LICENSED UNDER  [![License: MIT]
