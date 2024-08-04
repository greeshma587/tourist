from rest_framework import serializers
from . models import *

class touristserializers(serializers.ModelSerializer):
    spotimage = serializers.ImageField(required = False)


    class Meta:

        model = Tourist
        fields = ['id', 'spotname', 'place', 'city', 'state', 'country', 'googlemap', 'spotimage']

    def validate_spotimage(self, value):
        # Example validation
        if not value:
            raise serializers.ValidationError("No image provided")
        return value