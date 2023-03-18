from rest_framework import serializers
from watchapp.models import WatchList, StreamPlatforms,Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model= Review
        # fields = "__all__"
        exclude = ('watchList',)

class WatchSerializer(serializers.ModelSerializer):
    reviews= ReviewSerializer(many=True, read_only = True)
    #len_name=serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        # fields= "__all__" #takes all fields defined in model
        exclude= ['active']


# class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchSerializer(many=True,read_only=True) #1 Platform can have many movies

    #watchlist = serializers.StringRelatedField(many=True) 

    class Meta:
        
        model = StreamPlatforms
        fields= "__all__"
        #extra_kwargs = {'url': { 'lookup_field': 'platform'}}
        
 
    # #adding Custom fields in model via serializer
    # def get_len_name(self,object):
    #     return len(object.name)

    # #field Validation
    # def validate_name(self,value):
    #     if len(value)<2:
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value


    # #object Validation
    # def validate(self,data):
    #     if data["name"] == data["description"]:
    #         raise serializers.ValidationError("Name and description are same.")
    #     else:
    #         return data

# #Validators
# def description_length(value):
#     if len(value)<10:
#         raise serializers.ValidationError("Desctiption is too short")
#     return value
# c
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField(validators=[description_length])
#     active = serializers.BooleanField()



    