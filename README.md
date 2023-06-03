## Todolist App
![image](https://github.com/EASS-HIT-PART-A-2022-CLASS-III/todolist/assets/81169397/5343a35e-3c0b-4c2f-b446-e4393fe800f0)

Simple Todolist web application on 3 docker containers: 
* MongoDB image
* Backend with fastapi 
* Frontend with Streamlit
* (for testing with pytest)

## Video 
https://youtu.be/ctPAfq_3RiM

https://github.com/EASS-HIT-PART-A-2022-CLASS-III/todolist/assets/81169397/3a7830cd-6405-4c6f-a6b8-05e5e4bdc173


## Installation
1. Clone the repository to your local machine.
```
git clone https://github.com/EASS-HIT-PART-A-2022-CLASS-III/todolist.git
```
2. Make sure Docker is running.
```
docker --version
```
3. Run from the directory
```
cd todolist
docker-compose build (for the first time)
docker-compose up
```
4. Go to [localhost:8501 ](http://localhost:8501/) and start to make **YOUR TODO LIST** ! 


## Project Tree
![image](https://github.com/EASS-HIT-PART-A-2022-CLASS-III/todolist/assets/81169397/6db61ae6-7d95-48e1-99ac-4d5f07e932ea)

## Requirements
* Docker
* Python 3.10 +

## Design Diagram:
                  +-------------------+
                  |   Web Browser     |
                  +-------------------+
                           |
                           | HTTP Requests
                           |
                  +-------------------+
                  |   Frontend        |
                  +-------------------+
                           |
                           | API Requests
                           |
                  +-------------------+
                  |    Backend        |
                  |   (FastAPI)       |
                  +-------------------+
                           |
                           | Database Queries
                           |
                  +-------------------+
                  |    Mongo DB       |
                  +-------------------+
                           |
                           | Docker Commands
                           |
                  +-------------------+
                  |     Docker        |
                  +-------------------+
                           |
                           | Git Commands
                           |
                  +-------------------+
                  |       Git         |
                  +-------------------+
## Authors
*Yanir*
