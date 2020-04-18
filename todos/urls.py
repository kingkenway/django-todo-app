from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.list_todo_items),
    path('insert_todo/', views.insert_todo_item, name='insert_todo_item'),
    path('delete/<int:id>/', views.todo_delete, name='todo_delete'),
]