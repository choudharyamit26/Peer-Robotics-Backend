from django.urls import path
from .views import CreateFlightsView,GetAllFlightsView,GetFlightsDetailsView,UpdateFlightsView

app_name = 'src'


urlpatterns = [
    path('create-flight/',CreateFlightsView.as_view(),name='create-flight'),
    path('get-flights/',GetAllFlightsView.as_view(),name='get-flights'),
    path('update-flight/<int:pk>/',UpdateFlightsView.as_view(),name='update-flight'),
    path('get-flight-details/<int:pk>/',GetFlightsDetailsView.as_view(),name='get-flight-details')
]