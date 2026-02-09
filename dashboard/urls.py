from django.urls import path
from .views import dashboard_view, delete_task, edit_task

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('edit/<int:task_id>/', edit_task, name='edit_task'),  # Reusing dashboard_view for editing
]