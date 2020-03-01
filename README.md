# Python - Flask - REST API
Simple REST API using Python with CRUD functions.

## Requirements
1. Python 3.x
2. MariaDB
3. Flask
4. Flask-RESTful
5. PyMySQL
6. Postman

## How to Use
1. Clone this repository to your desired location.
2. Create the database.
   ```
   CREATE DATABASE tpt_dua;
   ```
3. Create the table.
   ```
   CREATE TABLE cinemas(
       id INT NOT NULL AUTO_INCEMENT,
       title VARCHAR(255) NOT NULL,
       year VARCHAR(5) NOT NULL,
       director VARCHAR(50) NOT NULL,
       PRIMARY KEY(id));
   ```
4. Run `api_host.py`.
5. Fire-up Postman.
   - **GET** Request (Index page)
     > https://localhost:port/
   - **GET** Request (All movies)
     > https://localhost:port/films
   - **GET** Request (Movies by id)
     > https://localhost:port/films/<int:id>
   - **GET** Request (Movies by title)
     > https://localhost:port/films/<string:title>
   - **GET** Request (Movies by year)
     > https://localhost:port/films/<string:year>
   - **GET** Request (Movies by director)
     > https://localhost:port/films/<string:director>
   - **POST** Request
     > https://localhost:port/films/<int:id>
   - **PUT** Request
     > https://localhost:port/films/<int:id>
   - **DEL** Request
     > https://localhost:port/films/<int:id>
6. Do-what-you-want-with-it!
