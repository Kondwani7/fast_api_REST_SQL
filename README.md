# fast_api_REST_SQL
This provides an introduction to creating a database with the sqlachlemy and connecting it to an api with fastapi.

To set up the virtual environment, in your terminal type Mac: "python -m venv venv" then "source venv\bin\activate" windows: "python -m venv venv" then "venv\Scripts\activate"

To install Flask and the uvicorn server:

'pip install fastapi' and 'pip install "uvicorn[standard]"'

after to run the server type in your terminal "uvicorn yourfile:app --reload"

For more info, follow https://fastapi.tiangolo.com/

to initialize the DB, in your terminal run
oython create_db.py
