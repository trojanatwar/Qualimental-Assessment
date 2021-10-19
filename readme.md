# Pyramid/Flask task

This task will demonstrate the understanding of the data models, views and rest API paradigms. The objectives are to setup virtual environment with Pyramid or Flask frameworks, add a model and a view, and create an endpoint with OpenAPI.

## Setup

* Python > 3.8 and virtual environment installed

* SQLite3 browser or similar https://sqlitebrowser.org/dl/

### Setup Python virtual environment

1. Download the ZIP file containing project code. Unzip the file to a location on your local machine

2. Use python3 -m venv venv to generate new virtual env

3. Use source venv/bin/activate to activate the environment

4. Use pip install -e . to Install packages in the setup.py. This will install the dependencies including Pyramid, Openapi and SQLAlchemy.

5. The database is Sqlite3 and is located in the root of the repository in db.db file

### Review the existing code

#### Models

1. Start by opening db.db in your SQLite browser and inspect the tables, you should see User and Page tables. User contains users. Page contains pages owned by users.

2. Open src/model.py file and inspect the model developed using SQLalchemy. It should be identical to the SQLalchemy tables specification.

#### Views

1. There are three existing views implemented, all of them are mock
   1. Login - accessed through /login route
   2. Logout - accessed through /logout route
   3. Wiki view - accessed through /wiki route

#### OpenAPI

1. Open openapi.yaml file and see how login and logout endpoints are specified

2. The endpoints are connected with views via routes

3. Visit localhost:8080/docs to access Swagger documentation
Start the application
    1. You are now able to start the Pyramid application using
   pserve development.ini (or venv/bin/pserve development.ini if you are not using source)
    2. The application will run on localhost:8080 (you should see 404 Not found error)

# Tasks

## Home

1. Visit page root / Can you explain why it triggers 404 Not found error?
-> In openapi.yaml file root "/" path was not configured with proper response, with that
   A root "/" route was not added in __init__.py file and designated view for the same route.

   I have updated openapi.yaml file __init__.py and view.py to work the root URL

## Login

1. When you visit localhost:8080/login login view is called. Where is this route specified?
-> /login route is configured in openapi.yaml file and __init__.py add_route configuration      
   method.

2. Given that you do not need to input username nor password, who are you logged in as?
-> Unauthenticated user.

## Listing of pages per user

1. First specify the endpoint for wiki_view view in openapi.yaml file. Please be careful on the endpont name, it must match the route specified in __init__.py file. The endpoint has to be a GET request which accepts one parameter user_id
-> Done.

2. Go to wiki_view and develop a listing view, which accepts one parameter: user id, searches for all pages of that user, and outputs a list of all pages with ID and title only. Return data as JSON.
    1. You can use one of the two ways to get the user_id parameter from request
        1. self.request.openapi_validated.parameters.query.get("q")
        2. self.request.openapi_validated.body["title"]
    2. Use SQLAlchemy ORM to filter Pages based on user_id
    3. Do not paginate the data, just output the entire list of titles in JSON format
-> Done.

3. Test the new view using URL in your browser localhost:8i080/wiki_view?user_id=1 for example
-> Done.

# Deliverables and acceptance criteria
1. Provide answers to the questions in this document
2. Zipped folder containing the developed codes 
    1. Added openapi.yaml specification for wiki_view
    2. Added logic for listing view in wiki_view