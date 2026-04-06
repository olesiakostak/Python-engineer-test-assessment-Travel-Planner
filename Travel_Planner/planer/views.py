from django.shortcuts import render
from rest_framework import viewsets
from .models import TravelProject, Place
from .serializers import TravelProjectSerializer, PlaceSerializer
from rest_framework.exceptions import ValidationError

class TravelProjectViewSet(viewsets.ModelViewSet):
    queryset = TravelProject.objects.all()
    serializer_class = TravelProjectSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.places.filter(visited=True).exists():
            raise ValidationError('Project cannot be deleted if it has at least one visited place')
        
        return super().destroy(request, *args, **kwargs)


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        project_id = self.request.query_params.get('project')
        if project_id:
            queryset = queryset.filter(project_id=project_id)
        return queryset
