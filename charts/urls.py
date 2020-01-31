from django.urls import path
from .views import HomePageView, ChartData, ChartData2

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('api/chart/data/', ChartData.as_view()),
    path('api/chart/data2/', ChartData2.as_view())
]
