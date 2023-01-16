# The Soccer App

This is a basic football API with players and teams.

You can interact with them via 
[Postman]("https://api.postman.com/collections/17143949-2d67e437-a117-4124-aa06-236e39f05714?access_key=PMAT-01GPP8YNJP8S97AXG9NPVMGDQW") or via [Swagger]("http://146.190.164.103/api/doc/")

This project has two main models and a CRUD for each:

- Player
- Team

Below you can find the database diagram.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)

## Run project

To run this project locally you just need to download it, position yourself in the project path and type:

```python
docker compose up --build
```

After that Docker will make their magic and the project will be executing:

```python
http://localhost:8000/admin/
http://localhost:8000/api/
http://localhost:8000/api/doc/
```

## Run tests

```bash
  docker-compose run web python manage.py test .
```

## Populate DB

The project has a script to populate the database, you just need to follow the instructions below:

Access to Django shell:

```python
docker compose run web python manage.py shell
```

Once inside, copy and paste the following code:

```python
from general.scripts.populate_db import run
run()
```

If everything it's ok, the console will display:

```python
¡Registers are created successfully!

New super user was added
username: admin
email: admin@example.com
password: admin_pass

¡Now you can play and interact with the API!
```

At the end just type:
```python
exit()
```

And execute the project again!

# DB Diagram
![DB Diagram](https://github.com/ArmandoVn/test_2_xerpa/blob/development/DB_Diagram.png)
