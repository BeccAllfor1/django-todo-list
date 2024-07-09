from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('', views.welcome, name='home'),
    path('index/', views.index, name='organiser'),
    path('remove_item/<str:item_id>/', views.removeTask, name="remove_item"),
    path('edit_item/<str:item_id>/', views.edit_task, name="edit_item"),
    path('respond/<int:todo_id>/', views.respond_to_todo, name='respond'),
]
