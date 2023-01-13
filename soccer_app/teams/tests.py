from general.tests import BaseTestCase
from .factories import TeamFactory

from general.factories import UserFactory


# Create your tests here.
class TeamViewsetTestCase(BaseTestCase):
    def setUp(self):
        self.user = UserFactory()
        self.team_1 = TeamFactory()
        for i in range(0, 9):
            TeamFactory(name=str(i))
        self.url = "/api/teams/"

    def test_list_view(self):
        """Test that the list view works correctly"""
        token = self.authenticate(self.user)
        response = self.client.get(self.url, HTTP_AUTHORIZATION=token)
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["count"], 10)

    def test_detail_view(self):
        """Test that the detail view works correctly"""
        token = self.authenticate(self.user)
        response = self.client.get(
            f"{self.url}{self.team_1.id}/", HTTP_AUTHORIZATION=token
        )
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEquals(data["name"], self.team_1.name)
        self.assertEquals(data["city"], self.team_1.city)
