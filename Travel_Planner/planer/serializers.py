from rest_framework import serializers
from .models import TravelProject, Place
import requests


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

    def validate(self, data):
        project = data.get('project')
        external_id = data.get('external_id')

        if project and project.places.count() >= 10:
            if self.instance is None:
                raise serializers.ValidationError('A project cannot have more than 10 places.')

        if external_id:
            api_url = f"https://api.artic.edu/api/v1/artworks/{external_id}"
            try:
                response = requests.get(api_url, timeout=5)
                if response.status_code != 200:
                    raise serializers.ValidationError(f"Place with external_id '{external_id}' does not exist in Art Institute API.")
                
            except requests.exceptions.RequestException:
                raise serializers.ValidationError("Error connecting to the Art Institute API.")
        
        return data


class TravelProjectSerializer(serializers.ModelSerializer):
    places = PlaceSerializer(many=True, read_only=True)
    is_completed = serializers.SerializerMethodField()

    class Meta:
        model = TravelProject
        fields = ['id', 'name', 'start_date', 'description', 'places', 'is_completed']

    def create(self, validated_data):
        places = validated_data.pop('places_data', [])
        
        project = TravelProject.objects.create(**validated_data)
        
        for place in places:
            Place.objects.create(project=project, **place)
            
        return project
    
    def get_is_completed(self, object):
        places = object.places.all()

        if not places:
            return False
        
        return all(place.visited for place in places) 