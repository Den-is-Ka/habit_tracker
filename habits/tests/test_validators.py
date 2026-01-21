from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from habits.models import Habit

User = get_user_model()


class HabitValidatorsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="validator",
            email="val@test.com",
            password="12345"
        )

    def test_pleasant_habit_cannot_have_reward(self):
        habit = Habit(user=self.user, place="ванна", time="21:00", action="ванна", is_pleasant=True, reward="шоколад")
        with self.assertRaises(ValidationError):
            habit.full_clean()
