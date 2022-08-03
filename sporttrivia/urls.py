
from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index, name='index'),
    path('search/', views.Search, name='search-detail'),
    path('report/', views.ReportProblem, name='report-problem' ),
    path('quiz/score/', views.ScoreDetail, name='score-detail'),
    path('quiz/<slug:slug>/', views.QuizDetail , name='quiz-detail'),
    path('quiz/<slug:slug>/scores/', views.QuizTopScores , name='quiz-scores-detail'),

]
