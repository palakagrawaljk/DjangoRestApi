from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class StreamPlatforms(models.Model):
    name=models.CharField(max_length=30)
    about=models.CharField(max_length=150)
    website=models.URLField(max_length=100)

    def __str__(self):
        return self.name

class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    #Like This video is available only on you tube platform, but you tube have multiple videos.
    platform = models.ForeignKey(StreamPlatforms,on_delete=models.CASCADE,related_name='watchlist') #Many to 1
    active = models.BooleanField(default=True) # movie published
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):  #if any object is accessed of Movie class, return movie name
        return self.title

class Review(models.Model): #1 to many
    rating= models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    watchList = models.ForeignKey(WatchList,on_delete=models.CASCADE,related_name="reviews")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating)+"-"+ self.watchList.title
                   

