from django.db import models


class Team(models.Model):
    team_type = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f'Team: {self.description}'


class Person(models.Model):
    name = models.CharField(max_length=100, blank=False)    
    teams = models.ManyToManyField(Team)

    def __str__(self):
        return f'Person: {self.name}'
