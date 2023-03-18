from watchapp.models import WatchList, StreamPlatforms,Review
from watchapp.api.serializers import WatchSerializer, StreamPlatformSerializer,ReviewSerializer
from rest_framework.response import Response
#from rest_framework.decorators import api_view #function based
from rest_framework import status
from rest_framework.views import APIView #class based

#from rest_framework import mixins
from rest_framework import generics

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self,serializer): #name of function predefined in documentation
        pk = self.kwargs.get('pk')
        movie = WatchList.objects.get(pk=pk)
        serializer.save(watchList=movie)
    

# Concrete View Class
class ReviewList(generics.ListAPIView):
    #queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchList = pk)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Using Mixins
# class ReviewList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# class ReviewList(APIView):
#     def get(self,request):
#         review=Review.objects.all()
#         serializer = ReviewSerializer(review,many=True)
#         return Response(serializer.data)
    
# class ReviewDetail(APIView):
#     def get(self,request,pk):
#         try:
#             reviews=Review.objects.get(pk=pk)
#         except Review.DoesNotExist:
#             return Response({'error':'Review not found'},status=status.HTTP_404_NOT_FOUND)
        
#         serializer=ReviewSerializer(reviews,context={'request':request})
#         return Response(serializer.data)

class StreamPlatformAV(APIView):
    def get(self,request):
        platform = StreamPlatforms.objects.all()
        serializer = StreamPlatformSerializer(platform,many=True,context={'request':request})
        return Response(serializer.data)

    def post(self,request):
        serializer=StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class StreamPlatformDetailAV(APIView):
    def get(self, request,pk):
        try:
            platform=StreamPlatforms.objects.get(pk=pk)
        except StreamPlatforms.DoesNotExist:
            return Response({'error':'Platform not found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer=StreamPlatformSerializer(platform,context={'request':request})
        return Response(serializer.data)

    def put(self, request,pk):
        platform=StreamPlatforms.objects.get(pk=pk)
        serializer=StreamPlatformSerializer(platform,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk):
        platform=StreamPlatforms.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WatchListAV(APIView):

    def get(self, request):
        movies=WatchList.objects.all()
        serializer=WatchSerializer(movies,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=WatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() #internally create fn is called.
            return Response(serializer.data) 
        else:
            return Response(serializer.errors)

class WatchDetailAV(APIView):
    def get(self, request,pk):
        try:
            movie=WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer=WatchSerializer(movie)
        return Response(serializer.data)

    def put(self, request,pk):
        movie=WatchList.objects.get(pk=pk)
        serializer=WatchSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk):
        movie=WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies=Movie.objects.all()
#         serializer=MovieSerializer(movies,many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer=MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save() #internally create fn is called.
#             return Response(serializer.data) 
#         else:
#             return Response(serializer.errors)

# @api_view(['GET','PUT','DELETE'])
# def movie_detail(request,pk):
#     if request.method == 'GET':
#         try:
#             movie=Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)
        
#         serializer=MovieSerializer(movie)
#         return Response(serializer.data)

#     if request.method=='PUT': #update
#         movie=Movie.objects.get(pk=pk)
#         serializer=MovieSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     if request.method=='DELETE': #delete
#         movie=Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)