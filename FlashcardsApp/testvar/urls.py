from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_flashcard_sets, name='list_flashcard_sets'),
    path('study/<int:set_id>/', views.study_flashcard_set, name='study_flashcard_set'),
    path('create/', views.create_flashcard_set, name='create_flashcard_set'),
]
