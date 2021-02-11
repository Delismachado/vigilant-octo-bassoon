from django.db import models


class Person(models.Model):
    name = models.CharField(default='n/a', max_length=100)
    phone = models.CharField(default='a', max_length=12)
    age = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return f'Person: {self.name}'


class Team(models.Model):
    name = models.CharField(default='n/a', max_length=100)
    team_type = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100, blank=False)
    persons = models.ManyToManyField(Person)

    def __str__(self):
        return f'Team: {self.name}'
