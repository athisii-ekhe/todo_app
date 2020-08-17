from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('complete-todo/<int:id>/', views.complete_todo, name='complete'),
    path('delete-completed-todo/', views.delete_completed_todo,
         name='del-completed-todo'),
    path('delete-all/', views.delete_all, name='delete-all-todos'),
    path('nav/', views.nav, name='nav')
]
