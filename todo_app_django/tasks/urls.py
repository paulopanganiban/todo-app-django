# from todo_app_django.tasks.views import updateTask
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    # why int:pk? dahil pk ang ginamit natin sa views
    path('update_task/<int:pk>/', views.updateTask, name="update_task"),
    path('delete/<int:pk>/', views.deleteTask, name="delete")
]
