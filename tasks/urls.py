from django.urls import path
from . import views

urlpatterns = [
    path('get/<int:project_id>/', views.get_tasks),
    path('update/', views.update_task),
    path('create/', views.create_task),
]