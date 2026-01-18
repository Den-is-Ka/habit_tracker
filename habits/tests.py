from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Habit

User = get_user_model()

class HabitTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@test.com", password="12345"
        )
        self.client.force_authenticate(self.user)

    def test_create_habit(self):
        response = self.client.post("/api/habits/habits/", {
            "place": "дом",
            "time": "10:00",
            "action": "зарядка",
            "period": 1,
            "duration": 60
        })
        self.assertEqual(response.status_code, 201)
