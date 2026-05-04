from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email='test@example.com', name='Test', team='marvel', is_superhero=True)
        self.assertEqual(user.email, 'test@example.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='marvel', description='Marvel superheroes')
        self.assertEqual(team.name, 'marvel')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user='test@example.com', type='run', duration=30, date='2024-01-01')
        self.assertEqual(activity.type, 'run')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(user='test@example.com', name='pushups', reps=10, sets=3, date='2024-01-01')
        self.assertEqual(workout.name, 'pushups')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(team='marvel', points=100)
        self.assertEqual(lb.team, 'marvel')
