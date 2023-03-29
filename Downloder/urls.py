from django.urls import path
from .views import Piechart,csvconverter,title_list,YouTubeMetadataView,get_all_meta_data,LoginAPI,LogoutAPI,RegisterAPI,similar_video,download_video
from knox import views as knox_views

urlpatterns = [
    #path('download/', download_video, name='download_video'),
    path('list/',title_list),
    path('scrape/<str:video_id>/', YouTubeMetadataView.as_view(), name='scraping'),
    path('csv/<str:video_id>/', csvconverter.as_view(), name='scraping'),
    path('display/', get_all_meta_data, name='display data'),
    path('download/', get_all_meta_data, name='display data'),
    path('chart/', Piechart.as_view()),
    path('similarvideo/', similar_video.as_view()),

    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', LogoutAPI.as_view(), name='logout'),
    path('register/', RegisterAPI.as_view(), name='register'),
]