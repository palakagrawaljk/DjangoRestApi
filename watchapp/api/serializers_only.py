from rest_framework import serializers
from watchapp.models import Movie

#Validators
def description_length(value):
    if len(value)<10:
        raise serializers.ValidationError("Description is too short")
    return value

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField(validators=[description_length])
    active = serializers.BooleanField()

    def create(self,validated_data): #serializers.save() calls this method
        return Movie.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description',instance.descrsniiption)
        instance.active = validated_data.get('active',instance.active)
        instance.save()
        return instance

    #field Validation
    def validate_name(self,value):
        if len(value)<2:
            raise serializers.ValidationError("Name is too short")
        else:
            return value


    #object Validation
    def validate(self,data):
        if data["name"] == data["description"]:
            raise serializers.ValidationError("Name and description are same.")
        else:
            return data