from django.urls import path, include
from . import views
urlpatterns = [
    path('task-list/', views.tasklist, name='tasklist'),

]
