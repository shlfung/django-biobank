from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('programs/', views.ProgramListView.as_view(), name='programs'),
    path('participants/', views.ParticipantListView.as_view(), name='participants'),
]

