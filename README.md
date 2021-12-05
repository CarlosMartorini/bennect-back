# Bennect Back End

<br>

## Clone Project
- Clone the project via terminal in the desired folder.
```json
git clone git@github.com:CarlosMartorini/bennect-back.git
```

<br>

## Enter The Project
- Run this command via terminal
```json
cd bennect-back
```

<br>

## Create Environments
- Run this command via terminal
```json
python -m venv venv --upgrade-deps
```

<br>

## Activate Environment
- Run this command via terminal
```json
source venv/bin/activate
```

<br>

## Install Dependencies
- With environments activate, run on terminal to install all dependencies
```json
pip install -r requirements.txt
```

<br>

## Create Migrate
- You need to run migrate to create your database, for that run the following command
```json
./manage.py migrate
```

<br>

## Run Project
- To run the project enter the following command
```json
./manage.py runserver
```
> Now you can open in your browser the path http://127.0.0.1:8000/ to access the Django REST Framework Root API

<br>

# Application working with the Front End

<br>

## Clone Front End Project
- Clone the project via terminal in the desired folder.
```json
git clone git@github.com:CarlosMartorini/bennect-front.git
```

<br>


## Enter The Project
- Run this command via terminal
```json
cd bennect-front
```

<br>


## Install Dependencies
- Run on terminal to install all dependencies
```json
yarn
```
<br>


## Run Project
- To run the project enter the following command
```json
yarn start
```
> Your browser will automatically open the application

<br>
