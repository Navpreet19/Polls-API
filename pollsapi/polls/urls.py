from django.urls import path
from . import views

urlpatterns = [
    path('polls/', views.QuestionList.as_view()),
    path('polls/<int:pk>/', views.QuestionDetail.as_view()),
]