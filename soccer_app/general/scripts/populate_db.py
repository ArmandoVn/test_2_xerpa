import random

from faker import Faker

from players.models import Player
from teams.models import Team

from django.contrib.auth.models import User

fake = Faker()


def run():
    # Creating teams
    for i in range(0, 10):
        Team.objects.create(
            name=fake.name(),
            city=fake.city(),
        )

    # Creating players
    teams = Team.objects.all()
    for i in range(0, 100):
        Player.objects.create(
            name=fake.name(), goals=fake.pyint(), team=random.choice(teams)
        )

    # Creating superuser
    User.objects.create_superuser("admin", "admin@example.com", "admin_pass")
    print("¡Registers are created successfully!")
    print("")
    print("New super user was added:")
    print("username: admin")
    print("email: admin@example.com")
    print("password: admin_pass")
    print("")
    print("¡Now you can play and interact with the API!")
