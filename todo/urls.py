from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('', views.index, name='home'),
    path('remove_item/<str:id>/', views.removeTask, name="remove_item")
] 