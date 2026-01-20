from django.core.exceptions import ValidationError
from django.test import TestCase
from django.contrib.auth import get_user_model
from habits.models import Habit

User = get_user_model()


class HabitModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="user@test.com",
            password="12345"
        )

    def test_duration_cannot_exceed_120(self):
        habit = Habit(user=self.user, place="дом", time="08:00", action="йога", duration=150)
        with self.assertRaises(ValidationError):
            habit.full_clean()

    def test_reward_and_related_cannot_coexist(self):
        pleasant = Habit.objects.create(user=self.user, place="ванна", time="21:00", action="ванна", is_pleasant=True)
        habit = Habit(
            user=self.user, place="дом", time="08:00", action="зарядка", reward="кофе", related_habit=pleasant)
        with self.assertRaises(ValidationError):
            habit.full_clean()
