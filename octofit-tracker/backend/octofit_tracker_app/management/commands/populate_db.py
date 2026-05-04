
from django.core.management.base import BaseCommand
from octofit_tracker_app.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Ensure unique index on email for users
        db = connection.cursor().db_conn.client['octofit_db']
        db.users.create_index('email', unique=True)

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='marvel', is_superhero=True),
            User(email='captain@marvel.com', name='Captain America', team='marvel', is_superhero=True),
            User(email='spiderman@marvel.com', name='Spider-Man', team='marvel', is_superhero=True),
            User(email='batman@dc.com', name='Batman', team='dc', is_superhero=True),
            User(email='superman@dc.com', name='Superman', team='dc', is_superhero=True),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='dc', is_superhero=True),
        ]
        User.objects.bulk_create(users)

        # Activities
        Activity.objects.create(user='ironman@marvel.com', type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user='ironman@marvel.com', type='swim', duration=20, date=timezone.now().date())
        Activity.objects.create(user='batman@dc.com', type='cycle', duration=45, date=timezone.now().date())
        Activity.objects.create(user='superman@dc.com', type='run', duration=60, date=timezone.now().date())

        # Workouts
        Workout.objects.create(user='spiderman@marvel.com', name='pushups', reps=20, sets=3, date=timezone.now().date())
        Workout.objects.create(user='superman@dc.com', name='squats', reps=15, sets=4, date=timezone.now().date())
        Workout.objects.create(user='wonderwoman@dc.com', name='lunges', reps=12, sets=3, date=timezone.now().date())

        # Leaderboard
        Leaderboard.objects.create(team='marvel', points=150)
        Leaderboard.objects.create(team='dc', points=120)

        self.stdout.write(self.style.SUCCESS('Database populated with superhero test data.'))
