# The Soccer App

This is a basic football API, you can interact with them via
[Postman]("#") or via [Swagger]("http://localhost:8000/api/doc/")

## Run project


## Run tests


## Populate DB

The project has a script to populate the db, you just need following the next instructions:

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

Now you can play and interact with the API!
```

Now just type:
```python
exit()
```

And execute the project again!

# DB Diagram


# Resources
