from django.urls import path, include
#from watchapp.api.views import movie_list, movie_detail #function based View
from watchapp.api.views import (WatchListAV, WatchDetailAV,
                                StreamPlatformAV,StreamPlatformDetailAV,
                                ReviewDetail,ReviewList,ReviewCreate)

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>',WatchDetailAV.as_view(), name='movie-detail'),
    path('stream/',StreamPlatformAV.as_view(), name='stream-platform'),
    path('stream/<int:pk>',StreamPlatformDetailAV.as_view(), name='stream-detail-platform'),
    # path('review/',ReviewList.as_view(),name='review-list'),
    # path('review/<int:pk>',ReviewDetail.as_view(),name = 'review-details'),
    path('stream/<int:pk>/review',ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>',ReviewDetail.as_view(), name='review-detail'), #shi krra
    path('stream/<int:pk>/review-create',ReviewCreate.as_view(), name='review-create'),
   
] 

