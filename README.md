## Hero Restaurant Containerized
In project tech-stack:
 -  Python 3.6
 -  Django 2.0
 -  Postgres 9.6
 -  Redis
 
Requirements
 - Docker Toolbox (for windows)
 
### Windows Docker instructions
(! Important ) Any docker-compose or docker-machine should be run under Docker Quickstart Terminal
1. Start Docker Quickstart Terminal
2. Build containers: 

        docker-compose build
3. Run django related commands:

	    docker-compose run web python3 manage.py makemigrations
	    docker-compose run web python3 manage.py migrate
4. Start services: 

        docker-compose up
5. In Docker Quickstart Terminal you will find the <IP> of the machine

### Project instructions

1. Inside project is found .env file, please find ALLOWED_HOSTS.
2. Append you <IP> in ALLOWED_HOSTS 

### Running Unit Tests 
Docker Services may not be running when running unittest 

    docker-compose run web python3 manage.py test -k
    
### Running API Endpoint Tests
This is done using Postman REST Client
Please download Postman Collection from
            
    https://www.getpostman.com/collections/67cea2d1dad0feaea246

Sample api call:
    
| Action   | Http Method | URL                                                                         | DATA                    |
|----------|-------------|-----------------------------------------------------------------------------|-------------------------|
| Create   | POST        | http://IP:8000/restaurant/                                                | {  "name": "Berlin 4" } |
| List     | GET         | http://IP:8080/restaurant/                                                |                         |
| Retrieve | GET         | http://IP:8080/restaurant/pk/                                           |                         |
| Update   | PUT         | http://IP:8000/restaurant/pk/                                           |                         |
| Delete   | DELETE      | http://IP:8000/restaurant/pk/                                           |                         |
    
    <IP> ===> Docker machine IP
    <pk> ===> Primary Key of Model Restaurant    
    Sample URL: http://192.168.99.100:8080/restaurant/1/        (pk=1)