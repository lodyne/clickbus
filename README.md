# ClickBus Services API

This is explanation on how to run and use the ClickBus Services API.

The application is built by using Django - A Python Backend Framework.

Also, it uses Django Rest Framework (DRF) - A library to create REST API
and other packages found in ```requirements.txt```.

## How to Run

Create new folder anywhere in your PC eg. In Desktop - create clickbus folder.
Open Command Prompt (cmd) in a path of created folder, then install package for
virtual environment.

### Install Virtual Environment

When dealing with django, it is advised to use virtual environment so as
to make sure the dependencies from various projects do not collide.
Eg. on windows: - ``` pip install virtualenvwrapper-win ```

PS: Make sure you have installed Python in your PC

### Make Virtual Environment

After installing virtual environment, you have to make vitual environment for your
preference. ```mkvirtualenv clickbus```

### Clone the Application

Then clone the entire application from github into the folder you created locally.
```git clone https://github.com/lodyne/clickbus.git```

## REST API

The REST API to the ClickBus app is described below.

### Get list of Places

#### Request 1

`GET /places/`
Endpoint: <http://localhost:8000/places/>

#### Response 1

    HTTP 200 OK
    Allow: GET, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept

    [...]

### Edit a Place

#### Request 2

`POST /place/new`

Endpoint: <http://localhost:8000/places/edit/1>

#### Response 2

    HTTP 200 OK
    Allow: GET, PUT, PATCH, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept

    {"name":Kisasa,"city":"Tabora","state":"Tanzania", "image":"tabora.jpg"}

### Create a new Place

#### Request 3

`POST /place/new`

Endpoint: <http://localhost:8000/places/new>

#### Response 3

    HTTP 200 OK
    Allow: GET, POST, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept

    {"name":Kihonda,"city":"Morogoro","state":"Tanzania", "image":"upload_file.jpg"}

### Get a specific Place

#### Request 4

`GET /place/id`

EndPoint: <http://localhost:8000/place/1>

#### Response 4

    HTTP 200 OK
    Allow: GET, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept

    {"name":Kikuyu,"city":"Dodoma","state":"Tanzania", "image":"dodoma.jpg"}

## Summary of EndPoints

    `GET/places/` - List Places: <http://localhost:8000/places/>
    `PUT/places/edit/1` - Edit Place: <http://localhost:8000/places/edit/1>
    `POST/places/new` - Create Place: <http://localhost:8000/places/new>
    `GET/places/1/` - Get Specific Place: <http://localhost:8000/place/1>
