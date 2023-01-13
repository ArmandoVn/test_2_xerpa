import factory

from faker import Faker
from .models import Team

fake = Faker()


class TeamFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Team

    name = factory.LazyAttribute(lambda _: fake.name())
    city = factory.LazyAttribute(lambda _: fake.city())
