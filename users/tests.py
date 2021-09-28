from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import CustomUser
# Create your tests here.

class User_HRTests(TestCase):
    def setUp(self):
        self.users = get_user_model().objects.create_user(
            username="HRBoost", email="HRBoost@outlook.com", password="HRBoost1234"
        )

    def test_user_create(self):
        email = self.users.email
        self.assertEquals(self.users.username.__str__(), "HRBoost")
        self.assertEquals(self.users.email.__str__(), "HRBoost@outlook.com")

    def test_duplicates(self):
        try:
            self.user = get_user_model().objects.create_user(
                username="HRBoost", email="HRBoost@outlook.com", password="HRBoost1234"
            )
        except:
            print("something wrong, this is a duplicated ")

    def test_none_user_creation(self):
        User = get_user_model()
        with self.assertRaises(Exception):
            User.objects.create_user(email='', password="HRBoost1234")