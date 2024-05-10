# TestTask

This README file describes the basic steps to run this project using Docker.

## Setup



### 1. Cloning the repository

First clone this repository to your computer:

```bash
https://github.com/nyko27/test_task.git
```

### 2. Creating .env file

1) Create an .env file in the root directory of the cloned project.
2) Write the required values to this file as shown in the example:


```bash
SECRET_KEY=<your_secret_key>
POSTGRES_DB=<db_name>
POSTGRES_USER=<db_user>
POSTGRES_PASSWORD=<db_password>
POSTGRES_HOST=db
```


<sub>`POSTGRES_HOST` is set to `db` because it is the name of the PostgreSQL service defined in the docker-compose file<sub>

### 3. Running project

Start the project running the following command in the root directory of the project
```bash
docker-compose up
```

Now the project is running and available at the following URL: http://0.0.0.0:8000/