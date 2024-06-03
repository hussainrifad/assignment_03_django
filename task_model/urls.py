from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_task, name = 'addtask'),
    path('delete/<int:id>', views.delete_task, name = 'deletetask'),
    path('update/<int:id>', views.update_task, name = 'updatetask')
]