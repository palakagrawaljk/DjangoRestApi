from django.contrib import admin
# from watchapp.models import Movie
from watchapp.models import WatchList,StreamPlatforms,Review
# Register your models here.
# admin.site.register(Movie)
admin.site.register(WatchList)
admin.site.register(StreamPlatforms)
admin.site.register(Review)
