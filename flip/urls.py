
from django.urls import path

from . import views

app_name = "flip"

urlpatterns = [
        path('', views.IndexView.as_view(), name='flip_index'),
        path('img/<str:image>/', views.get_image, name='flip_image'),
        ]
