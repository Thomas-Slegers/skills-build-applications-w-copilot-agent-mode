from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    is_superhero = models.BooleanField(default=False)
    def __str__(self):
        return self.email

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()
    def __str__(self):
        return f"{self.user} - {self.type}"

class Workout(models.Model):
    user = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    reps = models.IntegerField()
    sets = models.IntegerField()
    date = models.DateField()
    def __str__(self):
        return f"{self.user} - {self.name}"

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    def __str__(self):
        return f"{self.team} - {self.points}"