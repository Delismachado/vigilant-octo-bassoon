from rest_framework import viewsets
from .serializers import TeamSerializer, PersonSerializer
from .models import Team, Person


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('name')
    serializer_class = PersonSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by('description')
    serializer_class = TeamSerializer
