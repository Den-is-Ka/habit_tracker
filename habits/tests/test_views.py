from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from habits.models import Habit

User = get_user_model()


class HabitApiTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="apiuser",
            email="api@test.com",
            password="12345"
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

    def test_public_habit_list_visible(self):
        Habit.objects.create(user=self.user, place="дом", time="10:00", action="чай", is_public=True)
        response = self.client.get("/api/habits/habits/?public=true")
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.data["results"]), 0)
