from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('trainers/equation/', views.trainersEquation, name='trainersE'),
    path('trainers/numbers/', views.trainersNumbers, name='trainersN'),
    path('trainers/unequal/', views.trainersUnequal, name='trainersU'),
    path('equation1/select_difficulty/', views.select_difficulty, name='select_difficulty'),
    path('equation1/play_game/', views.play_game, name='play_game'),
]