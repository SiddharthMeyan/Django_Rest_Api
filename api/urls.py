from django.urls import path, include
from . import views
urlpatterns = [
    path('task-list/', views.tasklist, name='tasklist'),
    path('task-details/<str:pk>', views.taskDetails, name='taskDetails'),
    path('task-create', views.taskCreate, name='taskCreate'),
    path('task-delete/<str:pk>', views.taskDelete, name='taskDelete'),
    path('task-update/<str:pk>', views.taskUpdate, name='taskUpdate'),

]
